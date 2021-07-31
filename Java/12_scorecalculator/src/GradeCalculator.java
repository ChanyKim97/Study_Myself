import java.util.ArrayList;

public class GradeCalculator {
    private final String name;
    private final double PreAverage;
    private final int PreCredit;
    private int coursecredit;
    private double coursesum;
    private ArrayList<Course> list = new ArrayList<>();

    public GradeCalculator(String name, double PreA, int PreC){
        this.name = name;
        this.PreAverage = PreA;
        this.PreCredit = PreC;
        this.coursesum = 0;
        this.coursecredit = 0;
    }


    public void addCourse(Course a){
        list.add(a);

        coursesum += a.Score_Dou;
        coursecredit += a.CourseCredit;
    }



    public void print(){
        System.out.println("직전 학기 성적: " + PreAverage +" (총 " + PreCredit +"학점)");
        System.out.println("이번 학기 성적: " +(coursesum/coursecredit) + " (총 " + coursecredit +"학점)");
        System.out.println("전체 예상 성적: " + ((PreAverage * PreCredit) + coursesum*coursecredit)/(PreCredit+coursecredit) +" (총 " + PreCredit+coursecredit +"학점)");
    }
}