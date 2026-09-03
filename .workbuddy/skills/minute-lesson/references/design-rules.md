# Minute Lesson · Design Rules（生成规范）

本文件是 minute-lesson 的唯一风格与交互依据。生成 HTML 时**照抄**下列令牌与结构，不另起炉灶。目标：浅色极简、认知负担低、一次一题、来源可查。

## 1. 设计令牌（CSS 变量，直接使用）

```css
:root{
  --bg:#f7f8fa; --card:#ffffff; --ink:#1f2430; --sub:#6a7180;
  --line:#e6e8ee; --acc:#3d5af1; --acc-soft:#eef1fd; --acc-line:#cfd7f8;
  --mono:"Cascadia Code",Consolas,"Courier New",monospace;
  --ok:#137a4b; --ok-soft:#e8f5ef; --bad:#b4233f; --bad-soft:#fbeef1;
}
```

**配色纪律**：页面只允许 白/灰阶 + `--acc` 主蓝；仅判题反馈可用 `--ok/--bad`。禁止其它彩色（红橙黄绿紫随取随弃都是违规）。**禁止 emoji / 图标 / 渐变 / 阴影堆叠**；代码与路径用 `--mono` 灰底。

## 2. 页面骨架

```
.wrap（max-width:800px，padding 上下留白）
├─ .top       标题「<主题> 速成」+ 右侧徽标「读图约 X 秒 · 答题约 Y 秒」
├─ .lead      「Core Fact」小标签 + 大字核心事实(26px/800，含最常见误解纠偏) + 一句补充 + 三个要点词
├─ section 01 核心结构（目录树 / 解剖图，最能说明本质的一张图）
├─ section 02 补充维度（存放/参数/位置…，≤2 卡片）
├─ section 03 流程或步骤（需要时用单色 SVG 流程图）
├─ section 04 记忆口诀或两条原则
├─ section 05 自测（.quiz 卡片，见第 4 节）
├─ .sources   资料来源（见第 5 节，必需）
└─ footer     备注「依据官方文档编写 · 存于 <目录>」
```

分区标题带序号徽标 `.no`（01–05）。正文一律少字：卡片内不超过 3 行短句，能用图示就不用列表。

## 3. 图示规范

- **目录树 / 结构图**：`<div class="tree">` 等宽字体 + `white-space:pre`，行尾可加灰色注释；必需项用主蓝粗体标 `必需` 徽标，可选项灰字标 `可选`。参照实例页面 V4 的 tree 样式。
- **流程图**：SVG `viewBox="0 0 760 92"`；框=白底 `stroke:#e6e8ee`、文字 `#1f2430`（14px/700）+ 灰小字 `#8a909c`（11px）；箭头灰 `#c3c9d8`；唯一被强调的框可用 `fill:#f4f6fd;stroke:#3d5af1`。整图 2~4 步即可。

## 4. 分层自适应测验（核心机制）

### 4.1 规则定义

- 三个难度档：`1 初学 · 2 进阶 · 3 熟练`。题库每档 ≥3 题，共 ≥9 题。
- **起始档 = 2（进阶）**。
- 每题作答后：
  - 答对 → 连续答对数 `streak+1`；档位升一档（封顶 3）。若已在 3 档，维持 3。
  - 答错 → `streak` 清零；档位降一档（最低 1）。
- **提前结业**：`streak ≥ 3`（即连续答对 3 题）。
- **强制结业**：累计作答满 7 题。
- 取题：当前档未做题中取；该档已耗尽则向相邻档补未做题。
- 结业评级：提前结业 →「熟练通关」；否则按最后一题所在档位给评级：3 熟练 / 2 进阶 / 1 初学。评级为 1 时结语必须引导先回看正文再测。

### 4.2 UI 必备元素

- 顶部：第 n / 7 题、进度条、**难度指示器**（如 `○●○` 三格或文字"进阶"）、连续答对标记（🔥 禁止用 emoji → 用文字「连对 ×2」）。
- 一次只显示一题；点击选项即锁定并判分；下方展开解析；解析内可用「见资料来源」引用来源序号。
- 上一题不可回改（分层逻辑不允许回退）；提供"← 重做"整体重置。

### 4.3 JS 骨架（可直接嵌入）

```js
const LVL=["初学","进阶","熟练"];
const BANK=[ // 每档≥3
 {t:"…",o:["A","B","C","D"],a:1,e:"解析",lv:1},
 /* 更多 … */
];
let cur=null,lvl=2,streak=0,total=0,used=new Set(),done=false;
const pool=l=>BANK.filter(q=>q.lv===l&&!used.has(q));
function nextQ(){ // 当前档取题，耗尽向相邻档借
  let c=pool(lvl);
  if(!c.length)c=pool(Math.min(3,lvl+1));
  if(!c.length)c=pool(Math.max(1,lvl-1));
  if(!c.length){finish();return null;}
  cur=c[0];used.add(cur);total++;paintQ(cur);
}
function answer(i){
  if(done)return; const right=i===cur.a;
  if(right){streak++; if(lvl<3)lvl++;}
  else{streak=0; if(lvl>1)lvl--;}
  renderJudge(right,i);
  if(streak>=3||total>=7)finish();
  else setTimeout(nextQ,900); // 或由“下一题”按钮触发
}
function finish(){ /* 评级=streak>=3?'熟练通关':LVL[lvl-1]; 显示结果屏 */ }
```

## 5. 资料来源区（必需，不可省略）

- 位置：测验之后、页脚之前，标题「资料来源」+ 主蓝序号徽标风格。
- 列出 Step 1 收集的来源：`<a href=真实URL target=_blank rel=noopener>标题</a>` + 一行「依据：……」摘注。
- 至少 1 条权威来源；产品/框架类知识点必须含其官方文档链接。
- 页面 footer 注明「内容依据官方文档编写」。

## 6. 交付自检清单

- [ ] 来源链接 ≥1 且真实、可点击，已放「资料来源」区
- [ ] 常见误解已作为核心事实点出（如适用）
- [ ] 无 emoji、无多余彩色、图标克制（全部用文字/符号表达）
- [ ] 测验：三层题库 ≥9 题、答对升档/答错降档、streak≥3 或 7 题结业
- [ ] 单文件 HTML、中文、移动端可读（viewport 已设置）
- [ ] 已 present_files 预览并记入当日 memory
