import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("(I)ntro (C)ourses (E)xit");
            String get = scanner.next();
            switch (get) {
                case "e":
                case "E":
                    System.out.println("안녕히 가세요.");
                    break;
                case "i":
                case "I":
                    System.out.println("안녕하세요! 우리는 코드잇입니다.\n함께 공부합시다!");
                    break;
                case "c":
                case "C":
                    while (true) {
                        System.out.println("코드잇 수업을 소개합니다.");
                        System.out.println("(P)ython (J)ava (i)OS (B)ack");
                        String select = scanner.next();
                        switch (select) {
                            case "p":
                            case "P":
                                System.out.println("Python 언어를 통해 컴퓨터 사이언스의 기초를 배웁니다.\n강사: 강영훈\n추천 선수과목: 없음");
                                break;
                            case "j":
                            case "J":
                                System.out.println("Java의 기본 문법과 객체지향적 프로그래밍을 배웁니다.\n강사: 김신의\n추천 선수과목: Python");
                                break;
                            case "i":
                            case "I":
                                System.out.println("최신 Swift 언어를 통해 iOS 개발을 시작할 수 있습니다.\n강사: 성태호\n추천 선수과목: Python, Java");
                                break;
                            case "b":
                            case "B":
                                break;
                        }
                        if(select.equals("b") || select.equals("B")) break;
                    }
                    break;
            }
            if(get.equals("e") || get.equals("E")) break;
        }
    }
}
