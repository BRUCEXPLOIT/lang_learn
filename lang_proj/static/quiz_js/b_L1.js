  const questions = document.querySelectorAll(".question");
        const prevBtn = document.getElementById("prev-btn");
        const nextBtn = document.getElementById("next-btn");
        const submitBtn = document.getElementById("submit-btn");
        let currentQuestion = 0;

        function showQuestion(index) {
            questions.forEach((question, idx) => {
                question.classList.toggle("hidden", idx !== index);
            });
            prevBtn.disabled = index === 0;
            nextBtn.classList.toggle("hidden", index === questions.length - 1);
            submitBtn.classList.toggle("hidden", index !== questions.length - 1);
        }

        prevBtn.addEventListener("click", () => {
            if (currentQuestion > 0) {
                currentQuestion--;
                showQuestion(currentQuestion);
            }
        });

        nextBtn.addEventListener("click", () => {
            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                showQuestion(currentQuestion);
            }
        });

        showQuestion(currentQuestion);