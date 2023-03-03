<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import type { Question } from '@trivia-api/models'

/**
 * Helper function to get questions from The Trivia API
 * @returns an array of questions
 */
 const getQuestions = async () => {
  const response = await fetch(
    "https://the-trivia-api.com/api/questions?limit=10"
  );

  const questions = await response.json();

  return questions;
};

// store all questions on the current quiz
const questions = ref<Question[]>([])

// track the user's progress through the quiz
const currentQuestionIndex = ref<number>(0)

// track the user's current score
const score = ref<number>(0)

// derive the current question from the current index
const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])

// derive the remaining number of questions from the current index and the total number of questions
const remainingNumberOfQuestions = computed(() => questions.value.length - currentQuestionIndex.value)

// order all (correct & incorrect) answers alphabetically so the correct answer is shuffled with the incorrect answers
const allAnswers = computed<string[]>(() => [currentQuestion.value.correctAnswer, ...currentQuestion.value.incorrectAnswers].sort((a,b) => a < b ? -1 : 1))

// derive the state of the quiz from existing state
const quizState = computed< "not ready" | "in progress" | "complete">(() => {
  if (questions.value.length === 0) {
    return "not ready";
  } else if (remainingNumberOfQuestions.value > 0) {
    return "in progress";
  } else {
    return "complete";
  }
})

/**
 * Called when the user guesses an answer to update the score and 
 * show the next question.
 * @param guess - The user's guess
 */
  const handleGuessAnswer = (guess: string) => {
  if (guess === currentQuestion.value.correctAnswer) {
    score.value++;
  }

  currentQuestionIndex.value++;
};

/**
 * Reset the state so the user can play another quiz
 */
const resetQuiz = () => {
  questions.value = [];
  score.value = 0
  currentQuestionIndex.value = 0

  getQuestions().then((res) => {
    questions.value = res;
  });
};

// When the page loads, fetch questions from the API
onMounted(() => {
  getQuestions().then(res => questions.value = res)
})

</script>

<template>
  <div class="App">
    <header class="App-header">Trivia API Vue Starter</header>
    <p class="intro-paragraph">
      This site shows how to use
      <a href="https://the-trivia-api.com">The Trivia API</a> to build a basic
      quiz web app using <a href="https://vuejs.org/">Vue</a>. The code is
      public and can be seen on
      <a href="https://github.com/the-trivia-api/vue-starter">its Github repo</a
      >.
    </p>
    <table class="score-table">
      <tbody>
        <tr>
          <th>Total Questions</th>
          <td>{{ questions.length }}</td>
        </tr>
        <tr>
          <th>Current score</th>
          <td>{{ score }}</td>
        </tr>
        <tr>
          <th>Questions remaining</th>
          <td>{{ remainingNumberOfQuestions }}</td>
        </tr>
      </tbody>
    </table>
    <div v-if="currentQuestion" class="answer-question">
      <p class="answer-question__question">
        {{ currentQuestionIndex + 1 }}: {{ currentQuestion.question }}
      </p>
      <ul class="answer-question__answers">
        <li v-for="answer in allAnswers" :key="answer">
          <button @click="handleGuessAnswer(answer)">{{ answer }}</button>
        </li>
      </ul>
    </div>
    <details v-if="currentQuestion">
      <summary>Question JSON</summary>
      <pre class="question-json">
             {{ JSON.stringify(currentQuestion, null, 2) }}
            </pre
      >
    </details>
    <p v-if="quizState === 'not ready'">Loading questions...</p>
    <template v-if="quizState === 'complete'">
      <p>Complete! You scored {{ score }}/{{ questions.length }}</p>
      <button @click="resetQuiz">Play again</button>
    </template>
    <footer>
      <a href="https://the-trivia-api.com">The Trivia API</a>
      <a href="https://github.com/the-trivia-api/vue-starter">Github Repo</a>
    </footer>
  </div>
</template>

<style>
body {
  color: rgba(0, 0, 0, 0.8);
  background-color: #fef9f2;
}

.intro-paragraph {
  max-width: 70ch;
  margin: auto;
  text-align: left;
  margin-bottom: 2rem;
}

.App {
  text-align: center;
}

.App-header {
  background-color: #aed9e0;
  padding: 1rem;
  font-size: 2rem;
  margin-bottom: 2rem;
}

.score-table {
  margin: auto;
}

.answer-question {
  margin: 4rem 0;
}

.answer-question__question {
  font-size: 1.5rem;
}

.answer-question__answers {
  display: inline-grid;
  grid-gap: 1rem;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  list-style: none;
  width: 90vw;
  padding-left: 0;
}

/* So that on small screens the buttons aren't too small */
@media only screen and (max-width: 600px) {
  .answer-question__answers {
    grid-template-columns: 1fr;
  }
}

.answer-question__answers button {
  background-color: none;
  border: none;
  padding: 1rem;
  width: 100%;
  cursor: pointer;
}

.answer-question__answers > :nth-child(1) button {
  background-color: #ffa69e;
}

.answer-question__answers > :nth-child(2) button {
  background-color: #faf3dd;
}

.answer-question__answers > :nth-child(3) button {
  background-color: #b8f2e6;
}

.answer-question__answers > :nth-child(4) button {
  background-color: #aed9e0;
}

.question-json {
  text-align: left;
  width: min-content;
  margin: auto;
}

footer {
  background-color: #aed9e0;
  position: fixed;
  bottom: 0;
  display: flex;
  justify-content: space-evenly;
  width: 100vw;
  padding: 0.5rem 0;
}
</style>
