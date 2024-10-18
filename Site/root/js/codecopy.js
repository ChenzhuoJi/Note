 /* 复制代码功能 */
 function copyCode() {
    const codeBlock = document.querySelector('pre code').innerText;
    navigator.clipboard.writeText(codeBlock).then(() => {
        alert('代码已复制到剪贴板');
    }).catch(err => {
        alert('复制失败：' + err);
    });
}