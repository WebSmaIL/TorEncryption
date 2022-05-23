

confirmBtn.addEventListener("click", (e)=> {
    let right = 0;
    answers.forEach((el) => {
        input = document.getElementById(el);
        if (input.checked) {
            right++;
        }
    })
    modal.classList.add("active");
    document.querySelector(".progress-text").innerHTML = `${right} / ${answers.length}`;
})