public class Course {
    public static final int CREDIT_MAJOR = 3;
    public static final int CREDIT_GENERAL = 2;
    private final String CourseName;
    private final String Score_Str;
    public final int CourseCredit;
    public double Score_Dou;

    public Course(String name, int credit, String scr) {
        this.CourseName = name;
        this.CourseCredit = credit;
        this.Score_Str = scr;

        double score = 0;
        switch (Score_Str) {
            case "A+":
                score = 4.5;
                break;
            case "A":
                score = 4.0;
                break;
            case "B+":
                score = 3.5;
                break;
            case "B":
                score = 3.0;
                break;
            case "C+":
                score = 2.5;
                break;
            case "C":
                score = 2.0;
                break;
            case "D+":
                score = 1.5;
                break;
            case "D":
                score = 1.0;
                break;
            case "F":
                score = 0.0;
                break;
        }
        this.Score_Dou = score;
    }

}