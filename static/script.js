function handleFiles(files) {
    const formData = new FormData();
    formData.append("file", files[0]);

    fetch("/analyze/", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            data.is_spam ? "🚨 СПАМ" : "✅ НЕ СПАМ";
        document.getElementById("cleanedText").innerText = data.cleaned_text;
    })
    .catch(() => {
        alert("Ошибка при загрузке файла");
    });
}
