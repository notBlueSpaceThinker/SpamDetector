
// Получаем нужные элементы
const dropZone = document.getElementById("drop-area");
const fileInput = document.getElementById("fileElem");
const browseLink = document.getElementById("browse");

// Отключаем стандартное поведение для dnd
dropZone.addEventListener("dragenter", stopDefaults, false);
dropZone.addEventListener("dragover", stopDefaults, false);
dropZone.addEventListener("dragleave", stopDefaults, false);
dropZone.addEventListener("drop", stopDefaults, false);

function stopDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Наведение и убирание подсветки
dropZone.addEventListener("dragenter", function() {
    dropZone.classList.add("highlight");
}, false);

dropZone.addEventListener("dragover", function() {
    dropZone.classList.add("highlight");
}, false);

dropZone.addEventListener("dragleave", function() {
    dropZone.classList.remove("highlight");
}, false);

dropZone.addEventListener("drop", function() {
    dropZone.classList.remove("highlight");
}, false);

// Обработка сброса файла
dropZone.addEventListener("drop", function(e) {
    let files = e.dataTransfer.files;
    if (files && files.length > 0) {
        processFile(files[0]);
    }
}, false);

// Клик по ссылке вызывает input
browseLink.onclick = function() {
    fileInput.click();
};

// Файл выбран вручную
fileInput.onchange = function() {
    if (fileInput.files.length > 0) {
        processFile(fileInput.files[0]);
    }
};

// Обработка файла
function processFile(file) {
    if (!file) return;

    let formData = new FormData();
    formData.append("file", file);

    let result = document.getElementById("result");
    let text = document.getElementById("cleanedText");

    result.innerText = "Загружаю...";
    text.innerText = "";

    fetch("/analyze/", {
        method: "POST",
        body: formData
    }).then(function(res) {
        if (!res.ok) {
            return res.text().then(function(err) {
                throw new Error(err);
            });
        }
        return res.json();
    }).then(function(data) {
        result.innerText = data.is_spam ? "ну спамСПАМ" : "НЕ СПАМ";
        text.innerText = data.cleaned_text || "";
    }).catch(function(err) {
        result.innerText = "Ошибка анализа";
        text.innerText = err.message || "Неизвестная ошибка";
    })
}
