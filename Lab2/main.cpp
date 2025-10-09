#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
using namespace std;

struct Student {
    string nume_complet, spec;
    int an;
    float media;
};

void sorteaza(Student *tab[], int n,bool (* comparator)(Student*, Student*)) {

}

int main() {

    ifstream myFile("studenti.csv");
    string nume, prenume, spec, an, media;
    if (myFile.is_open()) {
        string line;
        while (getline(myFile,line)) {
            stringstream ss(line);

            getline(ss,nume,',');
            cout<<nume<<" ";

            getline(ss,prenume,',');
            cout<<prenume<<" ";

            getline(ss,spec,',');
            cout<<spec<<" ";

            getline(ss,an,',');
            cout<<an<<" ";

            getline(ss,media,',');
            cout<<media<<" ";

            cout<<endl;

        }
    }myFile.close();

    return 0;
}
