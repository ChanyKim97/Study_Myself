//public class PhoneBox extends Box<Phone> {
//    public void handsFreeCall(String numberString) {
//        object.call(numberString);
//    }
//}
public class PhoneBox<T extends Phone> extends Box<T> {
    public void handsFreeCall(String numberString) {
        object.call(numberString);
    }
}