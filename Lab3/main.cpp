#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
using namespace std;

class Student{
    string nume_complet, spec;
    int an;
    float media;
public:
    Student(string, string, int, float);
    static bool compNume(Student *, Student *); // funcție statică prin care se compară 2 studenți după nume
    static bool compMedia(Student *, Student *); // funcție statică prin care se compară 2 studenți după medie
    void afiseaza();
    friend class TabStudenti;
};
bool compNume(Studenti string &a, Student string &b) {
    return a.nume_complet<b.nume_complet;
}
bool compMedia(Studenti float &a, Student float &b) {
    return a.nume_complet<b.nume_complet;
}


class TabStudenti{
    int n; //numărul de studenți
    Student ** studenti; //pointer către tabloul de studenți
    int partitie(int, int, bool (*)(Student*, Student*)); //pentru quicksort
    void quicksort(int, int, bool (* comparator)(Student*, Student*));
    void bubblesort(int,int,bool (* comparator)(Student*, Student*));
public:
    TabStudenti(string);//citeste datele din fișierul al cărui nume e specificat prin parametru
    int getN(); //returnează numărul de studenți
    void afiseaza();
    void sorteaza(bool (*)(Student*, Student*));
    void sorteazaQ(bool (*)(Student*, Student*));
};

void sorteaza(int v[], int dim, bool tr) {
    bool sortat;
    int i,aux;
    do{
        sortat=true;
        for(i=0;i<dim-1;i++){
            if(v[i]>v[i+1]){
                aux=v[i];v[i]=v[i+1];v[i+1]=aux;
                sortat=false;
            }
        }
    }while(!sortat);
}
void sorteazaQ(int st, int dr, bool tr) {
    if(st < dr){
        int m = (st + dr) / 2;
        int aux = v[st];
        v[st] = v[m];
        v[m] = aux;
        int i = st , j = dr, d = 0;
        while(i < j){
            if(v[i] > v[j]){
                aux = v[i];
                v[i] = v[j];
                v[j] = aux;
                d = 1 - d;
            }
            i += d;
            j -= 1 - d;
        }
        quicksort(v, st , i - 1);
        quicksort(v, i + 1 , dr);
    }
}
void TabStudenti::afiseaza() {
    int i,dim=0;
    dim = getN();
    for (i=0;i<dim;i++)
        cout<<nume_complet<<" "<<spec<<" "<<an<<" "<<media<<"\n";
}

int main() {

    TabStudenti ts("studenti.txt");
    cout<<"\nAm citit " << ts.getN() << " studenti:"<<'\n';
    ts.afiseaza();

    cout<<"\nQuickSort Studentii sortati alfabetic:"<<'\n';
    ts.sorteazaQ(Student::compNume);
    ts.afiseaza();

    cout<<"\nQuickSort Studentii sortati dupa medii:"<<'\n';
    ts.sorteazaQ(Student::compMedia);
    ts.afiseaza();

    cout<<"\nBubbleSort Studentii sortati alfabetic:"<<'\n';
    ts.sorteaza(Student::compNume);
    ts.afiseaza();

    cout<<"\nBubbleSort Studentii sortati dupa medii:"<<'\n';
    ts.sorteaza(Student::compMedia);
    ts.afiseaza();

    return 0;
}