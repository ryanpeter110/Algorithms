#include <iostream>
using namespace std;
int size;
class Person
{
    string name;
    Person* partner;
    bool engaged;
    Person** prefList;
    int prefPosition;
    int prefEnd;

public:
    Person()
    {
        name = "";
        partner = NULL;
        engaged = false;
        prefList = new Person*[size];
        prefPosition = -1;
        prefEnd = -1;
    }
    bool isEngaged();
    bool prefers(Person *p);
    void engage(Person *p);
    void disengage();
    Person* getNextPref();
    string getName();
    void setName(string name);
    void addToPrefList(Person *p);
    Person* getPartner();
};
bool Person::isEngaged()
{
    return engaged;
}
bool Person::prefers(Person *p)
 {
    for (int i = 0; i < size; i++)
    {
        if (prefList[i]->getName() == p->getName())
            return true;
        if (prefList[i]->getName() == partner->getName())
            return false;

    }
    return false;
}

void Person::engage(Person *p)
{
    partner = p;
    engaged = true;
}

void Person::disengage()
{
    partner = NULL;
    engaged = false;
}

Person* Person::getNextPref()
{
    return prefList[++prefPosition];
}

string Person::getName()
{
    return name;
}

void Person::setName(string n)
{
    name = n;
}

void Person::addToPrefList(Person* p)
{
    prefList[++prefEnd] = p;
}

Person* Person::getPartner()
{
    return partner;
}

void displayArray(Person* p[])
{
    for(int i = 0; i < size; i++)
        {
                cout<<i<<" : "<<p[i]->getName()<<endl;
        }
                                                                                                                                      91,1          33%
}

bool singleMenLeft(Person* p[])
{
    for (int i = 0; i < size; i++)
        {
        if(!p[i]->isEngaged())
            return true;
        }
    return false;
}

int main()
{
    cout<<"Enter size : \n";
    cin>>size;
    Person *m[size];
    Person *w[size];
    for (int i = 0; i < size; i++)
        {
        m[i] = new Person();
        w[i] = new Person();
        }
    string name;
    cout<<"Enter the names of "<<size<<" men"<<endl;
    for (int i = 0; i < size; i++)
    {
        cin>>name;
        m[i]->setName(name);
    }
    cout<<"Enter the names of "<<size<<" women"<<endl;
    for (int i = 0; i < size; i++)
    {
        cin>>name;
        w[i]->setName(name);
    }

    for (int i = 0; i < size; i++)
    {
        cout<<"Enter the preference list for "<<m[i]->getName()<<endl;
        displayArray(w);
        for (int j = 0; j < size; j++)
        {
            int n;
            cin>>n;
                                                                                                                                      91,1          66%
            m[i]->addToPrefList(w[n]);
        }
    }
    for (int i = 0; i < size; i++)
    {
        cout<<"Enter the preference list for "<<w[i]->getName()<<endl;
        displayArray(m);
        for (int j = 0; j < size; j++)
        {
            int n;
            cin>>n;
            w[i]->addToPrefList(m[n]);
        }
    }
    while (singleMenLeft(m))
    {
        for (int i = 0; i < size; i++)
        {
            if (m[i]->isEngaged())
                continue;
            Person *woman = m[i]->getNextPref();
            if (!woman->isEngaged())
            {
                m[i]->engage(woman);
                woman->engage(m[i]);
            }
            else
            {
                if(woman->prefers(m[i]))
                 {
                    woman->getPartner()->disengage();
                    woman->disengage();
                    m[i]->engage(woman);
                    woman->engage(m[i]);
                }
            }
        }
    }
    for (int i = 0; i < size; i++)
    {
        cout<<m[i]->getName()<<" : "<<m[i]->getPartner()->getName()<<endl;
    }
return 0;

}
                                                                                                                                      182,1         Bot
