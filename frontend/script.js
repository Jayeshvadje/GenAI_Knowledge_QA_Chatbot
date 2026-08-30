const questionInput = document.getElementById("question");
const askButton = document.getElementById("ask-button");
const answerContainer = document.getElementById("answer-container");
const errorMessage = document.getElementById("error-message");


async function askQuestion() {
    const question = questionInput.value.trim();

    errorMessage.textContent = "";

    if (!question) {
        errorMessage.textContent = "Please enter a question.";
        return;
    }

    askButton.disabled = true;
    askButton.textContent = "Thinking...";

    answerContainer.innerHTML = marked.parse(data.answer);

    try {
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Unable to generate an answer."
            );
        }

        answerContainer.innerHTML = `
            <p>${data.answer}</p>
        `;

    } catch (error) {

        answerContainer.innerHTML = "";

        errorMessage.textContent =
            error.message || "Something went wrong.";

    } finally {

        askButton.disabled = false;
        askButton.textContent = "Ask";
    }
}


askButton.addEventListener("click", askQuestion);