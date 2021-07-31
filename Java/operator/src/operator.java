public class operator {
    public static void main(String[] args) {
        System.out.println("I am " + 27 + " years old.\nhi");
        System.out.println("The result is " + false + ".");

        System.out.println(9 / 5);
        System.out.println(9.0 / 5);

        //int a = 3;

        //System.out.println(-a);  // 양, 음 부호가 바뀜
        //System.out.println(++a); // a에 1을 추가
        //System.out.println(--a); // a에 1을 감소

        int a = 3;
        int b = 5;

        System.out.println(a > b);  // a가 b보다 크다
        System.out.println(a >= b); // a가 b보다 크거나 같다
        System.out.println(a < b);  // a가 b보다 작다
        System.out.println(a <= b); // a가 b보다 작거나 같다
        System.out.println(a == b); // a는 b와 같다
        System.out.println(a != b); // a는 b와 같지 않다

        double x = 3.14;
        int y = (int)x;

        long e = 123;
        long f = 123L;   // long의 리터럴 표현방법

        //float g = 3.14;  // 오류: 형이 맞지 않음. 필요한 값: float, 발견된 값: double
        float h = 3.14f; // float의 리터럴 표현방법
        float i = 314f;  // float의 리터럴 표현방법

        double j = 3.14;
        double k = 314d; // double의 리터럴 표현 방법

    }
}
