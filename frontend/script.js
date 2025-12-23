const form = document.getElementById("enter_frame");
const emailInput = document.getElementById("email");
const submitButton = document.getElementById("submit_button")
const url = "http://localhost:8000/newsletter/subscribe/api"

form.addEventListener("submit", async function (event) {
    event.preventDefault();
    if (event.submitter === submitButton) {
    submitButton.disabled = true;
    try {
        const email = emailInput.value.trim();
        const response = await fetch(url, {
            method: "POST",
            body: email
        });
            if (response.ok) {
                console.log("все ок")
            } else {
                console.error(await response.text());
            }
    } catch(error) {
                console.error(`ошибка при отправке ${error}`);
            } finally {
                submitButton.disabled = false;
            }
}})