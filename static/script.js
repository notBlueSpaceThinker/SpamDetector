// Обработка файла
function handleFiles(files) {
    if (!files.length) return;

    const formData = new FormData();
    formData.append("file", files[0]);

    // Очистка старого результата
    document.getElementById("result").innerText = "⏳ Анализ...";
    document.getElementById("cleanedText").innerText = "";

    // Файл через POST-запрос на сервер
    fetch("/analyze/", {
        method: "POST",
        body: formData
    })
    .then(async res => {
        if (!res.ok) {
            const errorData = await res.json();
            throw new Error(errorData.detail || "Неизвестная ошибка сервера");
        }
        return res.json();
    })
    .then(data => {
        // Отображение результатов
        document.getElementById("result").innerText =
            data.is_spam ? "🚨 СПАМ" : "✅ НЕ СПАМ";
        document.getElementById("cleanedText").innerText = data.cleaned_text;
    })
    .catch(err => {
        // Показываем текст ошибки, если есть
        document.getElementById("result").innerText = `❌ ${err.message}`;
        document.getElementById("cleanedText").innerText = "";
    });
}
