document.querySelectorAll(".uk-button").forEach(button => {
    button.addEventListener("click", () => {
        const targetId = button.getAttribute("target") + "-content";
        const data = document.getElementById(targetId);
        if (data) navigator.clipboard.writeText(data.value);
    })
})