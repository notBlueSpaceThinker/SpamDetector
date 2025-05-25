function handleFiles(files) {
    const formData = new FormData();
    for (let file of files) {
        formData.append("file", file);
    }

    fetch("/upload/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(result => {
        alert(`Файл ${result.filename} загружен!`);
    })
    .catch(error => {
        alert("Ошибка загрузки");
    });
}

document.getElementById("drop-area").addEventListener("dragover", (e) => {
    e.preventDefault();
});

document.getElementById("drop-area").addEventListener("drop", (e) => {
    e.preventDefault();
    handleFiles(e.dataTransfer.files);
});
