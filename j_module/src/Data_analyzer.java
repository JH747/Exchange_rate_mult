import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class Data_analyzer {
    public static void main(String[] args) throws Exception {

        List<String> origin_txt = new ArrayList<>();
        String str;

        int k = 1;
        while(true){
            TimeUnit.SECONDS.sleep(3);

            BufferedReader br = new BufferedReader(new FileReader("D:\\oh\\programming\\python_JAVA_multi\\data\\confirm.txt"));
            while((str = br.readLine()) != null){
                str = str.trim();
                if(str.length() >= 1){
                    //System.out.println(str);
                    origin_txt.add(str);
                }

            }
            br.close();

            String str1 = origin_txt.get(11).replace(",", "");
            String str2 = origin_txt.get(18).replace(",", "");
            float USD = Float.parseFloat(str1);
            float EUR = Float.parseFloat(str2);
            StringBuilder sb = new StringBuilder();
            sb.append("USD\n").append(USD).append("\n").append("EUR\n").append(EUR).append("\n");
            sb.append(Math.abs(USD-EUR));
            System.out.println(Math.abs(USD-EUR));

            BufferedWriter bw = new BufferedWriter(new FileWriter("D:\\oh\\programming\\python_JAVA_multi\\data\\analyzer_r.txt"));
            bw.write(sb.toString());
            bw.flush();
            bw.close();
        }

    }
}
