// This is a sample data.js file.
// Its contents can be replaced with the actual text data 
// needed for workout.html that pertains to 
// health and fitness.

// Notice that Questions have a "question_text" and several possible answers.
// Inside the answers are nested response questions and accompanying answers ("answer_text", what the user would click to respond).
// At some point a question will have no answers. It'll just be a response to the user that indicates
// the end of the loop (i.e., their program will have been determined and displayed)

var data = {
	"Question1": {
		"question_text": "Do you even lift?",
		"Answer1": {
			"answer_text": "Yeah.",
			"Question2": {
				"question_text": "Are you sure?",
				"Answer1": {
					"answer_text": "1.",
					"Question3": "Your program is..."
				},
				"Answer2": {
					"answer_text": "2.",
					"Question3": "Your program is..."
				},
				"Answer3": {
					"answer_text": "3.",
					"Question3": "Your program is..."
				}
			}
		},
		"Answer2": {
			"answer_text": "Nah.",
			"Question2": {
				"question_text": "Do you want to?",
				"Answer1": {
					"answer_text": "1.",
					"Question3": "Your program is..."
				},
				"Answer2": {
					"answer_text": "2.",
					"Question3": "Your program is..."
				},
				"Answer3": {
					"answer_text": "3.",
					"Question3": "Your program is..."
				}
			}
		},
		"Answer3": {
			"answer_text": "Maybe.",
			"Question2": {
				"question_text": "Decide.",
				"Answer1": {
					"answer_text": "1.",
					"Question3": "Your program is..."
				},
				"Answer2": {
					"answer_text": "2.",
					"Question3": "Your program is..."
				},
				"Answer3": {
					"answer_text": "3.",
					"Question3": "Your program is..."
				}			
			}
		}
	}
}