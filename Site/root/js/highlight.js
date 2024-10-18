// 动态引入 Highlight.js 的 CSS 样式
const link = document.createElement('link');
link.rel = 'stylesheet';
link.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/styles/monokai-sublime.min.css'; // 可更换为其他主题
document.head.appendChild(link);

// 动态引入 Highlight.js 的 JS 文件
const script = document.createElement('script');
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/highlight.min.js';
script.async = true;
script.onload = function() {
    // 当 Highlight.js 加载完成时，自动高亮所有代码块
    hljs.highlightAll();
};
document.head.appendChild(script);
