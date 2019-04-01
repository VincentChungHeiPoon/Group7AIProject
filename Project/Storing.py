#QMatrix/SARSA updates and storing written by Logan F.
from agent import Agent
from random import randint

#Ignore this using it for testing
w = 5
h = 5
d = 4
QMatrix = [[[0 for x in range(d)] for y in range(w)] for z in range(h)]

for x in range(0, 5):
    for y in range(0,5):
        for z in range(0,4):
            act = "";
            if z == 0:
                act = "North"
            if z == 1:
                act = "East"
            if z == 2:
                act = "South"
            if z == 3:
                act = "West"

            QMatrix[x][y][z] = 0

            print("Position = [", x, ", ", y, "], Direction = ", act, ", Value = ", QMatrix[x][y][z])
        print()


#Updating using Q-Learing
def Qpickupordropoff(i, j, q, newi, newj, alpha, gamma):
    QMatrix[i][j][q] = (1 - alpha) * (13-1) + gamma * max(QMatrix[newi][newj][0], QMatrix[newi][newj][1],
                                                      QMatrix[newi][newj][2], QMatrix[newi][newj][3]);
def Qmovespace(i, j, q, newi, newj, alpha, gamma):
    QMatrix[i][j][q] = (1 - alpha) * (-1) + gamma * max(QMatrix[newi][newj][0], QMatrix[newi][newj][1],
                                                      QMatrix[newi][newj][2], QMatrix[newi][newj][3]);

#Updating using SARSA
def SARSApickupordropoff(i, j, q, newi, newj, alpha, gamma):
    QMatrix[i][j][q] = QMatrix[i][j][q] + alpha(* (13-1) + (gamma*QMatrix[newi][newj][q] - QMatrix[i][j][q]));

def SARSAmovespace(i, j, q, newi, newj, alpha, gamma):
    QMatrix[i][j][q] = QMatrix[i][j][q] + alpha(*(-1) + (gamma * QMatrix[newi][newj][q] - QMatrix[i][j][q]));


def QUpdate(agent):
    #Receive Q-Matrix

    #rates
    gamma = 1.0;
    alpha = 0;

    #Previous location of the agent
    previ = agent.previ;
    prevj = agent.prevj;

    #Current location of the agent
    curri = previ;
    currj = prevj;

    #Direction the agent took
    q = 0;
    action = agent.direction
    if action == "North":
        q = 0;
        currj = prevj+1;
    if action == "East":
        q = 1;
        curri = previ+1;
    if action == "South":
        q = 2;
        currj = prevj-1;
    if action == "West":
        q = 3;
        curri = previ-1;

    #Update
    if (agent.ispickup == True):
        Qpickupordropoff(previ, prevj, q, curri, currj, alpha, gamma);
        SARSApickupordropoff(previ, prevj, q, curri, currj, alpha, gamma);
    else:
        Qmovespace(previ, prevj, q, curri, currj, alpha, gamma);
        SARSAmovespace(previ, prevj, q, curri, currj, alpha, gamma);

    #Send Q-Matrix back to file















