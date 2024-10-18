// 动态引入 MathJax 并配置 $$ 为公式识别符号
(function() {
    // 创建一个 <script> 元素用于加载 MathJax
    const script = document.createElement('script');

    // 设置 MathJax 的配置
    window.MathJax = {
        tex: {
            inlineMath: [['$', '$'],['\\(', '\\)']], // 使用 $ 作为行内公式符号
            displayMath: [['$$', '$$']], // 使用 $$ 作为块级公式符号
            processEscapes: true // 允许使用 '\' 来转义 '$'
        },
        svg: {
            fontCache: 'global' // SVG 的字体缓存设置
        }
    };

    // 设置加载 MathJax 的 CDN 路径
    script.src="https://polyfill.io/v3/polyfill.min.js?features=es6"
    script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
    script.async = true; // 异步加载 MathJax 脚本
    document.head.appendChild(script); // 将 <script> 标签插入到 <head> 中
})();
