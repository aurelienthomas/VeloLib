public class Station {
  int numero;
  String nom;
  String adresse;
  int latitude;
  int longitude;

  public Station(){
    this.numero = 0;
    this.nom = "";
    this.adresse = "";
    this.longitude = 0;
    this.latitude = 0;
  }
  public Station(int numero,String nom, String adresse, int latitude,int longitude){
    this.numero = numero;
    this.nom = nom;
    this.adresse = adresse;
    this.longitude = longitude;
    this.latitude = latitude;
  }

  public int getNumero(){
    return this.numero;
  }
  public void SetNumero(int numero){
    this.numero = numero;
  }
  public String getNom(){
    return this.nom;
  }
  public void SetNom(String nom){
    this.nom = nom;
  }
  public String getAdresse(){
    return this.adresse;
  }
  public void SetAdresse(String adresse){
    this.adresse = adresse;
  }
  public int getLongitude(){
    return this.longitude;
  }
  public void SetLongitude(int longitude){
    this.longitude = longitude;
  }
  public int getLatitude(){
    return this.latitude;
  }
  public void SetLatitude(int latitude){
    this.latitude = latitude;
  }
}
