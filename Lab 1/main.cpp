#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

//algoritmul de bubblesort in care elementul cu cea mai mare valoare din lista este mutat cu veciunul sau pana cand "iese la suprafata", adica ajunge la capatul vectorului, iar procesul se repeta
void bubble_sort(int v[], int dim){
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
//algoritmul de selectsort in care elementul cu cea mai mica valoare este mutat la inceputul vectorului, iar apoi se repeta termenii
void select_sort(int v[], int dim){
    int i,j,min,aux;
    for(i=0;i<dim-1;i++){
        min = i;
        for(j=i+1;j<dim;j++){
            if(v[j] < v[min])
                min = j;
        }
        if(min != i){
            aux = v[i];
            v[i] = v[min];
            v[min] = aux;
        }
    }
}
//algoritmul de quicksort, se alege un pivot, iar elementele mai mici decat pivotul se muta in stanga pivotului, cele mai mari in dreapta, iar procesul este recursiv pentru celelalte subvectori
void quick_sort(int v[], int st, int dr){
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
        quick_sort(v, st , i - 1);
        quick_sort(v, i + 1 , dr);
    }
}
//subprogramul care transforma string-ul de numere intr-un vector static pentru sortarea acestuia
int conversie_string_vector(string numere_fisier, int num[]) {
    int lungime = numere_fisier.length();
    int j = 0;
    num[j] = 0;

    for (int i = 0; i < lungime; i++) {
        if (numere_fisier[i] == ',') {
            j++;
            num[j] = 0;
        } else if (isdigit(numere_fisier[i])) {
            num[j] = num[j] * 10 + (numere_fisier[i] - '0');//transformam din caractere in numere
        }
    }
    return j + 1;//returnam dimensiunea vectorului
}
void afisare(int v[], int dim) {
    for (int i = 0; i < dim; i++)
        cout << v[i] << " ";
}

int main() {
    int varianta;
    int dim=0;
    int num[100];
    ifstream myFile("numere.csv");//deschdem fisierul numere.csv
    string line, numere_fisier = "";
    cout << "Sirul citit este: ";
    //prelucram fisierul csv, cand intalnim o virgula trecem la rand nou
    if (myFile.is_open()) {
        while (getline(myFile, line)) {
            stringstream ss(line);
            string number;
            while (getline(ss, number, ',')) {
                cout << number << ' ';
                numere_fisier += number + ",";
            }
        }
        myFile.close();

        //eliminam virgulele
        if (!numere_fisier.empty() && numere_fisier.back() == ',') {
            numere_fisier.pop_back();
        }

    }

    cout << '\n';

    //apelam functia de conversie, dim este dimensiunea vectorului static, numere_fisier string-ul de numere care e prelucrat, iar num este vectorul cre eapelat ca un parametru transmis prin pointer
    dim = conversie_string_vector(numere_fisier, num);

    cout << "Vectorul de numere este: ";
    afisare(num, dim);
    cout << '\n';

    cout << "Alege o optiune pentru a sorta numerele: 1)Bubblesort, 2)Selectsort, 3)Quicksort" << '\n';
    cin >> varianta;
    cout << '\n';

    //selectam algorimtul folosit
    switch (varianta) {
        case 1:
            bubble_sort(num, dim);
            break;
        case 2:
            select_sort(num, dim);
            break;
        case 3:
            quick_sort(num, 0, dim - 1);
            break;
        default:
            cout << "Optiune invalida!" << endl;
            return 1;
    }

    cout << "Sirul sortat este: ";
    afisare(num, dim);
    cout << endl;

    return 0;
}