public class array {
    public static void main(String[] args){
        int[] intArray = new int[5];
        intArray[0] = 1;
        intArray[1] = 2;
        intArray[2] = 3;
        intArray[3] = 4;
        intArray[4] = 5;

        System.out.println(intArray[0] + intArray[1]);

        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = arr1;
        arr1[0] = 100;
        System.out.println(arr2[0]);
        //같은 주소를 가리켜서 100이 출력됨
        //이를 해결하고복하하고 싶으면 arr1.clone(); 을 해주면 해결됨


        int[] intArray2 = new int[100];
        for (int i = 0; i < intArray2.length; i++) {
            intArray2[i] = i + 1;
        }
        for (double i : intArray2) {
            System.out.println(i);
        }

        String[] fruitsArray = new String[5];

        fruitsArray[0] = "딸기";
        fruitsArray[1] = "당근";
        fruitsArray[2] = "수박";
        fruitsArray[3] = "참외";
        fruitsArray[4] = "메론";

        for (String fruit : fruitsArray) {
            System.out.println(fruit);
        }

        String dna = "agagaga" + "cdcdcdcd";
        char[] chararray = dna.toCharArray();
        for(int i =0; i< chararray.length; i++){
            System.out.println(chararray[i]);
        }
    }
}
