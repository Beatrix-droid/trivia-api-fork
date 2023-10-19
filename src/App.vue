<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import type {Question} from './questionInterface';



// const hamburgerButton= document.getElementById("hamburger");
const navList = document.getElementById("nav");

// // toggle hamburger menu
// function toggleButton() {
//     navList!.classList.toggle("show")
// }

// hamburgerButton!.addEventListener("click", toggleButton);

/**
 * Helper function to get questions from The Trivia API
 * @returns an array of questions relating to fruits
 */
 const getQuestions = async (): Promise<Question[]> => {
  const filePath: string = './questions/italianTranslation.json';

    const response = await fetch(filePath);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

        //now select 10 random questions from the json:

    const data = await response.json();
    // Step 2: Create an empty array to store selected elements
    const selectedElements = [];
    // Step 3: Generate 10 unique random indices
    while (selectedElements.length < 10) {
    const randomIndex = Math.floor(Math.random() * data.length);
    
    // Step 4: Check for uniqueness
    if (selectedElements.indexOf(randomIndex) === -1) {
      selectedElements.push(randomIndex);
    }
  }

  // Step 5: Push the selected elements into a new array
    const arrTenQuestions = selectedElements.map(index => data[index]);

    // You can use the 'data' variable in your application
    // For example, update your UI with the JSON data here

    return arrTenQuestions; // Return the parsed JSON data

};

// store all questions on the current quiz
const questions = ref<Question[]>([])

// track the user's progress through the quiz
const currentQuestionIndex = ref<number>(0)

// track the user's current score
const score = ref<number>(0)
const scoreNum= Number(score);
// derive the current question from the current index
let currentQuestion = computed(() => questions.value[currentQuestionIndex.value])


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

/*
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

  getQuestions().then((data) => {
    console.log(data)
  });
};

// When the page loads, fetch questions from the API
onMounted(() => {
  getQuestions().then(res => questions.value = res)
})


</script>

<template>
  <div class="App">
<div class="navbar">
<ul id="nav"><li><a href="https://lokal.farm/unisciti-a-lokal-farm/">Unisciti a Lokal.farm</a></li>
<li><a href="https://lokal.farm/frutta-verdura/prodotti-stagione/">Prodotti di Stagione</a></li>
<li ><a href="https://lokal.farm/blog/">Blog</a></li>

</ul> 
<button class="hamburger" id="hamburger">
                    <i class="fa fa-bars"></i>
                </button>
</div>
    <header class="App-header" id="main-header">LOKAL FARM TRIVIA</header>

    <p class="intro-paragraph">
      Ottieni almeno 80% delle risposte corrette per vincere un premio!
    </p>
    <img src="https://lokal.farm/wp-content/uploads/2022/02/cropped-lokal-farm-frutta-e-verdura-a-km-0.png" alt="logo" class="logo">
    <table class="score-table">
      <tbody>
        <tr>
          <th>Totale Domande</th>
          <td>{{ questions.length }}</td>
        </tr>
        <tr>
          <th>Il tuo punteggio fin'ora</th>
          <td id="total scoe">{{ score }}</td>
        </tr>
        <tr>
          <th>Domade rimanenti</th>
          <td>{{ remainingNumberOfQuestions }}</td>
        </tr>
      </tbody>
    </table>
    <div v-if="currentQuestion" class="answer-question">
      <p class="answer-question__question">
        {{ currentQuestionIndex + 1 }}: {{ currentQuestion.question.text}}

        <!--{{ currentQuestionIndex + 1 }}: {{ currentQuestion.question}}-->
      </p>
      <ul class="answer-question__answers">
        <li v-for="answer in allAnswers" :key="answer">
          <button @click="handleGuessAnswer(answer)">{{ answer }}</button>
        </li>
      </ul>
    </div>
 
    <p v-if="quizState === 'not ready'">Caricamento quiz...</p>
    <template v-if="quizState === 'complete'">
      <p>Quiz Completato! Hai ottenuto {{ score }}/{{ questions.length }} risposte giuste!</p>
    
      <div id="centerDiv">
        <form id="frm" action="https://formsubmit.co/da4833c2fc5e05cf2b842f3ba7964ce0" method="POST">
     
          <p v-if="Number(score)<=7">Mi spiace non hai vinto il coupon ma… (puoi sempre fare un primo ordine registrandoti <a href="  https://lokal.farm/unisciti-a-lokal-farm">sul sito</a> o inserendo i tuoi dettagli qui per ricevere uno sconto del 10% sul primo ordine):</p>
        <input  v-if="Number(score)<=7" type="hidden" name="_autoresponse" value="Utilizza il codice QUIZ25 per ottenere un sconto del 10% sul tuo prossimo ordine!">

      <p v-if="Number(score)>7 && Number(score)<9 ">Congratulazioni, hai vinto! Lascia la tua mail e ti invieremo uno coupon per uno sconto del: 20%</p>
        <input  v-if="Number(score)>7" type="hidden" name="_autoresponse" value="Utilizza il codice QUIZ25 per ottenere un sconto del 20% sul tuo prossimo ordine!">
     
        <p v-if="Number(score)>8 && Number(score)<10">Congratulazioni, hai vinto! Lascia la tua mail e ti invieremo uno coupon per uno sconto del: 30%</p>
      <input  v-if="Number(score)>8" type="hidden" name="_autoresponse" value="Utilizza il codice QUIZ25 per ottenere un sconto del 30% sul tuo prossimo ordine!">

      <p v-if="Number(score)>9">Congratulazioni, hai vinto! Lascia la tua mail e ti invieremo uno coupon per uno sconto del: 40%</p>
      <input  v-if="Number(score)>9" type="hidden" name="_autoresponse" value="Utilizza il codice QUIZ25 per ottenere un sconto del 40% sul tuo prossimo ordine! ">

      <input type="hidden" name="_subject" value="Lokal Bot buono da spedire!"><br>
     <input type="text" name="name" placeholder="name" required>
     <br>
     <input type="email" name="email" placeholder="email" required>
     <br>
     <br>
     <textarea rows = "5" cols = "60" name = "message">
            -Commenti opzionali-
     </textarea><br>
     <br>
     <input type="hidden" name="_next" value="https://lokal-trivia-app.onrender.com/grazie.html">
     <button type="submit">Invia i tuoi dati</button>
 
</form> 
</div>
    </template>
    <div class="secondColour">
      <br>
      <h4><span style="color: #ffffff;"> CONTATTI:</span></h4>
          <p>sales@lokal.farm</p>
          <p>info@lokal.farm</p>
    </div>
    <footer>
      <a href="https://the-trivia-api.com">The Trivia API</a>
      <a href="https://github.com/the-trivia-api/vue-starter">Forked from this Github Repo</a>
    </footer>
  </div>
</template>

<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Roboto:wght@700&display=swap');

@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");

body {
  color: rgba(0, 0, 0, 0.8);
  background-color: #fef9f2;
}
.elementor-nav-menu--toggle {
  --menu-height: 100vh;
}

.secondColour{

            background-color: rgb(180, 219, 143);
            width:100%;
            height:23vh;
            border-top-left-radius: 10%;
            border-top-right-radius: 10%;
            color: white;
            position: absolute;
            bottom: 0px;
            
        
}

#centerDiv{
  line-height: 400px;
  text-align:center; 
  vertical-align:middle;
}
#frm{
  display: inline-block;
  vertical-align: middle;
  line-height: 14px; 
}
.intro-paragraph {
  max-width: 70ch;
  margin: auto;
  text-align: left;
  margin-bottom: 2rem;
}

.App {
  text-align: center;
  color:rgb(123, 185, 47);
  font-family: "Roboto", sans-serif;
}


.App-header {
  padding: 1rem;
  font-size: 2rem;
  margin-bottom: 2rem;
  font-weight: 700;
}

#main-header {
  margin-top: 2em;
}

.score-table {
  margin: auto;
}

.answer-question {
  margin: 4rem 0;
}

.answer-question__question {
  font-size: 1.5rem;
  font-family:"Quicksand", sans-serif;
  color: rgb(249, 152, 28);
font-style: italic;
font-weight: 500;
line-height: 42px
}

.answer-question__answers {
  display: inline-grid;
  grid-gap: 1rem;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  list-style: none;
  width: 90vw;
  padding-left: 0;
}

.answer-question__answers ul {
  border-radius: 12px;
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
  border-radius: 12px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.answer-question__answers > :nth-child(2) button {
  background-color: #faf3dd;
  border-radius: 12px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.answer-question__answers > :nth-child(3) button {
  background-color: #b8f2e6;
  border-radius: 12px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.answer-question__answers > :nth-child(4) button {
  background-color: #aed9e0;
  border-radius: 12px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

#hamburger {
    display: none
}

    @media screen and (max-width:641px) {
      #hamburger {
        display: inherit;
        float: right;
        left: 0;
        margin-right: 10px;
      }
    }



.navbar {
 
  overflow: hidden;
            
            
        }

@media screen and (max-width:641px) {

  .navbar li {

   display: none;

  }
}

.navbar li {
    list-style: none; 
    margin: 0 20px;
    flex: 1;
    text-align: center;
    float: right;
   }
.navbar a:hover::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background-color: rgb(123, 185, 47);
        }


.navbar a {
            color: black;
            font-weight: bold;
            text-decoration: none;
            margin: 0 20px;
            position: relative;
        }
.logo{
            position: absolute;
            top: 0;
            left: 0;
            width: 20%; /* Adjust this value to your desired width */
            height: auto;
        }

input[type=text] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

input[type=email] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

textarea {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
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
