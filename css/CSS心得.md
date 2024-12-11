### CSS心得

body最好设为**overflow:hidden;**这样就不会出现最大页面的滑动框

color才是字体颜色

```css
body {
    margin:0px;
    display: flex; /* 使用flex布局，使子元素水平排列 */
    font-family: Arial, sans-serif; /* 设置页面的默认字体 */
    height: 100vh;
    overflow:hidden;
    color:#404040;
    }
```

常见css

```css
text-align: center;  /* 文本居中对齐 */
border: 1px solid #ddd; /* 添加边框 */
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
border-radius: 8px; /* 添加圆角 */
font-size: 14px;    /* 设置文字大小 */
color: #444444;     /* 设置文字颜色 */
font-weight: bold;  /* 设置文字加粗 */
font-weight: normal; /* 确保表头字体不加粗 */
border: none; /* 移除按钮边框 */
cursor: pointer; /* 鼠标悬停时显示为指针 */
transition: background-color 0.3s; /* 设置背景颜色的过渡效果 */
white-space: nowrap;/* 不允许换行 */
user-select: none;/* 不允许选择文字 */
top: 20% !important;/* 与容器顶部的距离 */
overflow: auto;/* 允许滚动，建议父容器为hidden，且子容器要设置宽度 */
table-layout:fixed;
 z-index: 1000; /* 页面最上面 */
```

### 常见flex属性

flex: 1；可以搭配overflow：hidden；使用

```css
flex-direction: column; /* 子元素垂直排列 */
align-items: center; /* 子元素水平居中 */
flex-shrink: 0;   /* 元素不会缩小 */ 
.filter-button:hover {
    background-color: #edf9f7; /* 鼠标悬停时改变背景颜色 */
    border-bottom-color: #2d6253; 
}
flex: 1 ; /* 占据剩余的宽度 */
justify-content: space-between;/* 占满一行 */
gap: 10px 20px; /* 设置行间距为10px，列间距为20px */
```

技巧：可以搭配js实现宽度变化

```css
.sidebar-container.expanded {width: 16%; /* 扩展后的宽度 */}
```

```js
document.getElementById('filterButton').addEventListener('click', function() {
            sidebar.classList.toggle('expanded');
            tb1.classList.toggle('expanded');
            this.textContent = this.textContent === '»' ? '«' : '»';
        });
```

技巧：改变列宽

将单元格设为如下

```css
overflow: hidden;
text-overflow: ellipsis; /* ... */
```

想要改变列宽必须设为fixed；`table-layout` 是一个控制表格布局算法的 CSS 属性。它有两个主要值：

1. **auto**（默认值）：表格及其列的宽度根据内容动态调整。
2. **fixed**：表格及其列的宽度根据表格的宽度和列的宽度定义来确定，不考虑内容。

由于 `table-layout: fixed;` 的布局计算仅依赖于表格和列的宽度定义，而不依赖于内容，因此它能够显著加快表格的渲染速度，特别是在大数据量的表格中。

这里的技巧是color:white;这样不会影响表格的美观

```css
th .resize-handle {
    position: absolute;
    right: 0;
    bottom: 0;
    width: 5px;
    height: 100%;
    cursor: col-resize;
    z-index: 1;
    color:white;
}
```

技巧：表格置顶

outline是为了修复滑动时失去边界的bug

当元素使用 `position: sticky` 时，它的表现如下：

- 元素在容器内是相对定位的，当滚动到某个阈值时，它变成固定定位。
- 该元素会在父元素的特定位置（由 `top`, `right`, `bottom`, `left` 属性定义）开始“粘滞”。

```css
th{
    position:sticky;
    top:0;
    border: none;
    outline-color: #ddd;
    outline-style: solid;
    outline-width: 1px;
    background-color: white; /* 设置表头背景颜色 */
    user-select: none; /* 标准语法 */
    z-index: 1;  /* 确保表头在内容上方 */
}
```



