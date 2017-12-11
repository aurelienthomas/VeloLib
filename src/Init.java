import java.util.ArrayList;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Init {

	public static void main(String[] args) {
		ArrayList <Station>listeStation = new ArrayList<>();

	}

	GsonBuilder gsonb = new GsonBuilder();
	        gsonb.registerTypeAdapter(Station.class, new StationDeserializer());
	        Gson gson = gsonb.create();

}
