// for debugging modular pieces of code in app.vue

const getQuestions = async () => {
  const response = await fetch(
    "./src/questions/italianTranslation.json"
  )

  const questions = await response.json();
  console.log(questions)
  }