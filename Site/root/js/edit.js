// 添加新的标题
function addTitle() {
    var articleContent = document.getElementById("articleContent");
    var newTitle = document.createElement("h1");
    newTitle.setAttribute("contenteditable", "true");
    newTitle.textContent = "新的可编辑标题";
    articleContent.appendChild(newTitle);
}

// 添加新的段落
function addParagraph() {
    var articleContent = document.getElementById("articleContent");
    var newParagraph = document.createElement("p");
    newParagraph.setAttribute("contenteditable", "true");
    newParagraph.textContent = "这是一个新的可编辑段落。";
    articleContent.appendChild(newParagraph);
}

// 保存标题和段落内容
function saveContent() {
    var titles = Array.from(document.querySelectorAll(".art-cont h1")).map(h1 => h1.innerHTML);
    var paragraphs = Array.from(document.querySelectorAll(".art-cont p")).map(p => p.innerHTML);
    
    localStorage.setItem("savedTitles", JSON.stringify(titles));
    localStorage.setItem("savedParagraphs", JSON.stringify(paragraphs));
    
    alert("内容已保存！");
}

// 加载保存的标题和段落内容
function loadContent() {
    var savedTitles = JSON.parse(localStorage.getItem("savedTitles"));
    var savedParagraphs = JSON.parse(localStorage.getItem("savedParagraphs"));
    
    if (savedTitles && savedParagraphs) {
        var articleContent = document.getElementById("articleContent");
        articleContent.innerHTML = "";  // 清空现有内容
        
        // 重新添加保存的标题
        savedTitles.forEach(function(title) {
            var newTitle = document.createElement("h1");
            newTitle.setAttribute("contenteditable", "true");
            newTitle.innerHTML = title;
            articleContent.appendChild(newTitle);
        });
        
        // 重新添加保存的段落
        savedParagraphs.forEach(function(paragraph) {
            var newParagraph = document.createElement("p");
            newParagraph.setAttribute("contenteditable", "true");
            newParagraph.innerHTML = paragraph;
            articleContent.appendChild(newParagraph);
        });
    } else {
        alert("没有保存的内容！");
    }
}
// 复制当前HTML代码，并将contenteditable设置为"false"
function copyHTML() {
    // 查找所有带有contenteditable的元素，并将其设置为"false"
    document.querySelectorAll('[contenteditable]').forEach(function(element) {
        element.setAttribute('contenteditable', 'false');
    });

    // 获取修改后的HTML内容
    var htmlContent = document.getElementById('articleContent').outerHTML;

    // 将内容复制到剪贴板
    navigator.clipboard.writeText(htmlContent).then(function() {
        alert('HTML代码已复制到剪贴板！');
    }).catch(function(err) {
        console.error('复制失败: ', err);
    });
}