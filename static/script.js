// Получаем нужные элементы
const dropZone = document.getElementById("drop-area");
const fileInput = document.getElementById("fileElem");
const browseLink = document.getElementById("browse");

// Отключаем стандартное поведение для dnd
["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
    }, false);
});

// Подсветка зоны при перетаскивании
dropZone.addEventListener("dragenter", () => dropZone.classList.add("highlight"), false);
dropZone.addEventListener("dragover", () => dropZone.classList.add("highlight"), false);
dropZone.addEventListener("dragleave", () => dropZone.classList.remove("highlight"), false);
dropZone.addEventListener("drop", (e) => {
    dropZone.classList.remove("highlight");
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        processFile(files[0]);
    }
}, false);

// Клик по ссылке вызывает input
browseLink.onclick = () => fileInput.click();

// Обработка выбора файла вручную
fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
        processFile(fileInput.files[0]);
    }
};

// Обработка файла
function processFile(file) {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const result = document.getElementById("result");
    const text = document.getElementById("cleanedText");

    result.innerText = "Загружаю...";
    text.innerText = "";

    fetch("/analyze/", {
        method: "POST",
        body: formData
    }).then(res => {
        if (!res.ok) {
            return res.text().then(err => { throw new Error(err); });
        }
        return res.json();
    }).then(data => {
        result.innerText = data.is_spam ? "СПАМ" : "НЕ СПАМ";
        text.innerText = data.cleaned_text || "";
    }).catch(err => {
        result.innerText = "Ошибка анализа";
        text.innerText = err.message || "Неизвестная ошибка";
    });
}
