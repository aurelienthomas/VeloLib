public class StationDeserializer implements JsonDeserializer<Station> {

    public Station deserialize(JsonElement json, Type typeOfT,
            JsonDeserializationContext context) throws JsonParseException {
        Station out = new Station();

        if (json != null) {
            JsonObject obj  = json.getAsJsonObject();
            Set<Map.Entry<String,JsonElement>> entries = obj.entrySet();
            for (Map.Entry<String, JsonElement> e: entries) {
                if (e.getKey().equals("allAllowedChildren")) {
                    Type ft = List.class;
                    System.out.println(context.deserialize(e.getValue(), ft));
                    // TODO add this back into the Station out object
                } else {
                    // LocalLocationId
                    System.out.println(e.getKey());
                    System.out.println(context.deserialize(e.getValue(), Station.LocalLocationId.class));

                    // TODO add this back into the Station out object
                }
            }
        }
        return out;
    }

}
