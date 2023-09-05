

export interface Question {
    category: string
    id: string
    correctAnswer: string
    incorrectAnswers: string[]
    question: QuestionBody
    tags: string[]
    type: string
    difficulty: string
    regions: any[]
    isNiche: boolean
  }
  
  export interface QuestionBody {
    text: string
  }
  