public class ifelse {
    public static void main(String[] args){
        int number = 13;
        if (number % 2 == 0) {
            System.out.println("even number");
        } else {
            System.out.println("odd number");
        }

        int x = 10;
        int y = 1;

        if (x != 10 || x % 2 != 0) {
            System.out.println(x);
        } else if (y == 1) {
            System.out.println(y);
        } else {
            System.out.println(x + y);
        }


        int i = 10;
        if (i % 3 == 0) { // i < 20 : 불린 식, 변수, 메소드
            System.out.println("C 구역입니다.");
        } else if (1 % 3 == 1) {
            System.out.println("A 구역입니다.");
        } else {
            System.out.println("B 구역입니다.");
        }

        switch (i % 3) { // i : 불린이 아닌 식, 변수, 메소드
            case 0:
                System.out.println("C 구역입니다.");
                break;
            case 1:
                System.out.println("A 구역입니다.");
                break;
            default:
                System.out.println("B 구역입니다.");
                break;
        }


    }
}
