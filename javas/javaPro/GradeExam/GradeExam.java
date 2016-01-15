public class GradeExam {
	public static void main(String[] args) {
		char[][] answers = {
			{'A','B','A','C','D','D','E','A','C','D'},
			{'A','B','B','A','C','D','C','C','B','A'},
			{'A','B','C','C','A','C','B','D','B','A'},
			{'A','B','A','D','C','B','C','C','A','C'},
			{'A','B','A','C','D','A','C','B','C','A'},
			{'A','B','B','A','C','D','B','A','D','C'},
			{'A','B','A','C','D','C','B','C','A','D'},
			{'A','B','A','C','D','C','B','C','A','D'},
           
		};
        char[] keys = {'A','B','A','C','D','C','B','C','A','D'};
        for (int i = 0;i < answers.length;i++)
        {
            int yesCount = 0;
            for (int j =0;j < answers[i].length;j++)
            {
                if(answers[i][j] == keys[j])
                        yesCount++;
            }
            System.out.println("Student " + i + "\'s correct count                            is " + yesCount);
        }
            
            


	}
}
