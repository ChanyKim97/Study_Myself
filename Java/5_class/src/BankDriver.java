public class BankDriver {
    public static void main(String[] args){
        //사람선언
//        Person p1 = new Person();
//        p1.name = "김찬휘";
//        p1.age = 25;
//        p1.cashAmount = 30000;
//        p1.setAge(25);
//        p1.setName("김찬휘");
//        p1.setCashAmount(100000);
        Person p1 = new Person("김신의", 25);
        p1.setCashAmount(30000);
        Person p2 = new Person("문종모", 25, 100000);
        BankAccount a1 = new BankAccount(p1);
        a1.setBalance(100000);
        BankAccount a2 = new BankAccount(500000, p2);
        p1.setAccount(a1);
        p2.setAccount(a2);

        p2.transfer(p1, 200000);
        p1.transfer(p2, 150000);
        p2.transfer(p1, 270000);
        p1.transfer(p2, 130000);

//        System.out.println(p1.name);
//        System.out.println(p1.age);
//        System.out.println(p1.cashAmount);
//        BankAccount a1 = new BankAccount();
//        a1.balance =1000000;

//        a1.setBalance(500000);
//        p1.account = a1;
//        a1.owner = p1;

//        p1.setAccount(a1);
//        a1.setOwner(p1);
//
//        a1.deposit(30000);
//        a1.withdraw(170000);
//        a1.deposit(620000);
//        a1.withdraw(890000);




//        System.out.print(p1.name + "의 계좌 잔액: " + p1.account.balance);
//        Person p2 = new Person();
//        p2.name = "김찬휘";
//        p2.age = 25;
//        p2.cashAmount = 100000;
//
//        BankAccount a2 = new BankAccount();
//        a2.balance = 500000;
//
//        p2.account = a2;
//        a2.owner = p2;
//
//        a2.deposit(30000);
//        a2.withdraw(170000);
//        a2.deposit(620000);
//        a2.withdraw(890000);
    }
}