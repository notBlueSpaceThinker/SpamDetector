// Получаем нужные элементы
const dropZone = document.getElementById("drop-area");
const fileInput = document.getElementById("fileElem");
const browseLink = document.getElementById("browse");

// Отключаем стандартное поведение для dnd
const dragEevents = ["dragenter", "dragover", "dragleave", "drop"]
dragEevents.forEach(eventName => {
    dropZone.addEventListener(eventName, (event) => {
        event.preventDefault();
        event.stopPropagation();
    });
});

// Подсветка зоны при перетаскивании
["dragenter", "dragover"].forEach(eventName => {
    dropZone.addEventListener(eventName, () => {
        dropZone.classList.add("highlight");
    });
});

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("highlight");
});

// Обработка сброса файла
dropZone.addEventListener("drop", (event) => {
    dropZone.classList.remove("highlight");

    const files = event.dataTransfer.files;
    handleFileList(files);
});

// Клик по ссылке вызывает input
browseLink.onclick = () => fileInput.click();

// Обработка выбора файла вручную
fileInput.onchange = () => {
    handleFileList(fileInput.files);
};

// Обработка принятия файла
function handleFileList(files) {
    if (files.length === 0) {
        alert("Файл не найден!");
        return;
    }

    if (files.length > 1) {
        alert("Выберите только 1 файл");
        return;
    }

    processFile(files[0]);
}

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
