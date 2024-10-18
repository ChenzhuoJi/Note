// 获取所有div元素
let divs = document.querySelectorAll(".arcbox");

// 遍历每个div并替换文本
divs.forEach(function(divs) {
    let text = divs.innerHTML;

    // 先替换四个星号为加粗 <strong>（双星号优先）
    text = text.replace(/\*\*([^\*]+)\*\*/g, "<strong>$1</strong>");

    // 再替换两个星号为斜体 <em>
    text = text.replace(/\*([^\*]+)\*/g, "<em>$1</em>");

    // 将井号转换为标题，根据井号数量设置标题级别
    text = text.replace(/(#+)\s*(.*)/g, function(match, hashes, content) {
        let level = hashes.length; // 井号的数量决定标题级别
        if (level <= 6) {
            return `<h${level}>${content.trim()}</h${level}>`; // 将井号替换为标题标签
        } else {
            return match; // 超过6个井号保持原样
        }
    });

    // 将空的<p>标签替换为双换行
    text = text.replace(/<p>\s*<\/p>/g, "<br><br>");

    // 更新div中的HTML
    divs.innerHTML = text;
});
