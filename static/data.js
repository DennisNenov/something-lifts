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
		"question_text": "Do wish to gain weight, lose weight, or maintain?",
		"Answer1": {
			"answer_text": "Gain.",
			"Message": "Bulking Diet: \
						Calories: TDEE + 500 calories \
						Protein: 1+ grams per lb. bodyweight"
		},
		"Answer2": {
			"answer_text": "Lose.",
			"Message": "Cutting Diet: \
						Calories: TDEE - 500 calories \
						Protein: 1.5+ grams per lb. bodyweight"
		},
		"Answer3": {
			"answer_text": "Maintain.",
			"Message": "Maintenance: \
						Calories: TDEE \
						Protein: 1.25+ grams per lb. bodyweight"		
			}
		}
}
/*
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
*/