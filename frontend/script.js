const form = document.getElementById("enter_frame");
const emailInput = document.getElementById("email");
const submitButton = document.getElementById("submit_button")
const url_post_subscribers = "http://localhost:8000/newsletter/subscribe/"


form.addEventListener("submit", async function(event) {
    event.preventDefault();
    if (event.submitter === submitButton) {
    submitButton.disabled = true;
    const email = emailInput.value.trim();
    try {
        const formData = {
            "email": email
        }
        const response = await fetch(url_post_subscribers, {
            method: "POST",
            headers: {"Content-type": "application/json"},
            body: JSON.stringify(formData)
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


const tv_shows_Button = document.getElementById("tv_shows_Button");
const digital_Button = document.getElementById("digital_Button");
const url_get_tv_shows = "http://localhost:8000/categories/tv_shows"
const url_get_digital = "http://localhost:8000/categories/digital"



tv_shows_Button.addEventListener("click", async function() {
    try {
        const response = await fetch(url_get_tv_shows)
        const data = await response.json()
        if (response.ok) {
            console.log("все ок", data)
        } else {
            console.error(await response.text());
        }
    } catch(error) {
        console.error(`ошибка при отправке ${error}`);
    } finally {}
});


digital_Button.addEventListener("click", async function() {
    try {
        const response = await fetch(url_get_digital)
        const data = await response.json()
        if (response.ok) {
            console.log("все ок", data)
        } else {
            console.error(await response.text());
        }
    } catch(error) {
        console.error(`ошибка при отправке ${error}`);
    } finally {}
});