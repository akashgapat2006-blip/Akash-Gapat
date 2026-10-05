function checkQuiz() {
  let score = 0;
  const form = document.forms['quizForm'];

  if (form['q1'].value === "Waterfall") score++;
  if (form['q2'].value === "Software Development Life Cycle") score++;

  document.getElementById("result").innerText = "Your score: " + score + "/2";
}
