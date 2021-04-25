{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>V1</th>\n",
       "      <th>V2</th>\n",
       "      <th>V3</th>\n",
       "      <th>V4</th>\n",
       "      <th>V5</th>\n",
       "      <th>V6</th>\n",
       "      <th>V7</th>\n",
       "      <th>V8</th>\n",
       "      <th>V9</th>\n",
       "      <th>...</th>\n",
       "      <th>V21</th>\n",
       "      <th>V22</th>\n",
       "      <th>V23</th>\n",
       "      <th>V24</th>\n",
       "      <th>V25</th>\n",
       "      <th>V26</th>\n",
       "      <th>V27</th>\n",
       "      <th>V28</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.359807</td>\n",
       "      <td>-0.072781</td>\n",
       "      <td>2.536347</td>\n",
       "      <td>1.378155</td>\n",
       "      <td>-0.338321</td>\n",
       "      <td>0.462388</td>\n",
       "      <td>0.239599</td>\n",
       "      <td>0.098698</td>\n",
       "      <td>0.363787</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.018307</td>\n",
       "      <td>0.277838</td>\n",
       "      <td>-0.110474</td>\n",
       "      <td>0.066928</td>\n",
       "      <td>0.128539</td>\n",
       "      <td>-0.189115</td>\n",
       "      <td>0.133558</td>\n",
       "      <td>-0.021053</td>\n",
       "      <td>149.62</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.0</td>\n",
       "      <td>1.191857</td>\n",
       "      <td>0.266151</td>\n",
       "      <td>0.166480</td>\n",
       "      <td>0.448154</td>\n",
       "      <td>0.060018</td>\n",
       "      <td>-0.082361</td>\n",
       "      <td>-0.078803</td>\n",
       "      <td>0.085102</td>\n",
       "      <td>-0.255425</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.225775</td>\n",
       "      <td>-0.638672</td>\n",
       "      <td>0.101288</td>\n",
       "      <td>-0.339846</td>\n",
       "      <td>0.167170</td>\n",
       "      <td>0.125895</td>\n",
       "      <td>-0.008983</td>\n",
       "      <td>0.014724</td>\n",
       "      <td>2.69</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.0</td>\n",
       "      <td>-1.358354</td>\n",
       "      <td>-1.340163</td>\n",
       "      <td>1.773209</td>\n",
       "      <td>0.379780</td>\n",
       "      <td>-0.503198</td>\n",
       "      <td>1.800499</td>\n",
       "      <td>0.791461</td>\n",
       "      <td>0.247676</td>\n",
       "      <td>-1.514654</td>\n",
       "      <td>...</td>\n",
       "      <td>0.247998</td>\n",
       "      <td>0.771679</td>\n",
       "      <td>0.909412</td>\n",
       "      <td>-0.689281</td>\n",
       "      <td>-0.327642</td>\n",
       "      <td>-0.139097</td>\n",
       "      <td>-0.055353</td>\n",
       "      <td>-0.059752</td>\n",
       "      <td>378.66</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.0</td>\n",
       "      <td>-0.966272</td>\n",
       "      <td>-0.185226</td>\n",
       "      <td>1.792993</td>\n",
       "      <td>-0.863291</td>\n",
       "      <td>-0.010309</td>\n",
       "      <td>1.247203</td>\n",
       "      <td>0.237609</td>\n",
       "      <td>0.377436</td>\n",
       "      <td>-1.387024</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.108300</td>\n",
       "      <td>0.005274</td>\n",
       "      <td>-0.190321</td>\n",
       "      <td>-1.175575</td>\n",
       "      <td>0.647376</td>\n",
       "      <td>-0.221929</td>\n",
       "      <td>0.062723</td>\n",
       "      <td>0.061458</td>\n",
       "      <td>123.50</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.0</td>\n",
       "      <td>-1.158233</td>\n",
       "      <td>0.877737</td>\n",
       "      <td>1.548718</td>\n",
       "      <td>0.403034</td>\n",
       "      <td>-0.407193</td>\n",
       "      <td>0.095921</td>\n",
       "      <td>0.592941</td>\n",
       "      <td>-0.270533</td>\n",
       "      <td>0.817739</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.009431</td>\n",
       "      <td>0.798278</td>\n",
       "      <td>-0.137458</td>\n",
       "      <td>0.141267</td>\n",
       "      <td>-0.206010</td>\n",
       "      <td>0.502292</td>\n",
       "      <td>0.219422</td>\n",
       "      <td>0.215153</td>\n",
       "      <td>69.99</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 31 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Time        V1        V2        V3        V4        V5        V6        V7  \\\n",
       "0   0.0 -1.359807 -0.072781  2.536347  1.378155 -0.338321  0.462388  0.239599   \n",
       "1   0.0  1.191857  0.266151  0.166480  0.448154  0.060018 -0.082361 -0.078803   \n",
       "2   1.0 -1.358354 -1.340163  1.773209  0.379780 -0.503198  1.800499  0.791461   \n",
       "3   1.0 -0.966272 -0.185226  1.792993 -0.863291 -0.010309  1.247203  0.237609   \n",
       "4   2.0 -1.158233  0.877737  1.548718  0.403034 -0.407193  0.095921  0.592941   \n",
       "\n",
       "         V8        V9  ...       V21       V22       V23       V24       V25  \\\n",
       "0  0.098698  0.363787  ... -0.018307  0.277838 -0.110474  0.066928  0.128539   \n",
       "1  0.085102 -0.255425  ... -0.225775 -0.638672  0.101288 -0.339846  0.167170   \n",
       "2  0.247676 -1.514654  ...  0.247998  0.771679  0.909412 -0.689281 -0.327642   \n",
       "3  0.377436 -1.387024  ... -0.108300  0.005274 -0.190321 -1.175575  0.647376   \n",
       "4 -0.270533  0.817739  ... -0.009431  0.798278 -0.137458  0.141267 -0.206010   \n",
       "\n",
       "        V26       V27       V28  Amount  Class  \n",
       "0 -0.189115  0.133558 -0.021053  149.62      0  \n",
       "1  0.125895 -0.008983  0.014724    2.69      0  \n",
       "2 -0.139097 -0.055353 -0.059752  378.66      0  \n",
       "3 -0.221929  0.062723  0.061458  123.50      0  \n",
       "4  0.502292  0.219422  0.215153   69.99      0  \n",
       "\n",
       "[5 rows x 31 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "creditcard  = pd.read_csv('creditcard.csv')\n",
    "creditcard.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "creditcard = creditcard.drop(\"Time\", axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import preprocessing\n",
    "scaler = preprocessing.StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "creditcard['std_Amount'] = scaler.fit_transform(creditcard['Amount'].values.reshape (-1,1))\n",
    "\n",
    "\n",
    "creditcard = creditcard.drop(\"Amount\", axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Class', ylabel='count'>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZcAAAEGCAYAAACpXNjrAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/Z1A+gAAAACXBIWXMAAAsTAAALEwEAmpwYAAASUklEQVR4nO3df+xdd13H8eeLliH+GCuuztFOOrWa1Clla7bFX0GIW7fEFHSQzUgrLlTDZoQQwjDGkeESjSIyfswMV9YSZE4mrsZibQaKJg73HU72S7KvE1ybsZa1biiZ0vH2j/v5srvu9ttvx+fe2377fCQn99z3+ZzP+dykyavnnM8531QVkiT19LxpD0CStPgYLpKk7gwXSVJ3hoskqTvDRZLU3dJpD+BYceqpp9aqVaumPQxJOq7cddddX6mq5YfWDZdm1apVzMzMTHsYknRcSfKlUXUvi0mSujNcJEndGS6SpO4MF0lSd4aLJKk7w0WS1J3hIknqznCRJHVnuEiSuvMJ/Y7Oedu2aQ9Bx6C7fn/jtIcgTZxnLpKk7gwXSVJ3hoskqTvDRZLUneEiSerOcJEkdWe4SJK6M1wkSd0ZLpKk7gwXSVJ3hoskqTvDRZLUneEiSerOcJEkdWe4SJK6M1wkSd0ZLpKk7gwXSVJ3hoskqTvDRZLUneEiSepubOGS5Iwkn05yf5L7kvxGq78zyZ4kd7fl4qF93pFkNskXklw4VF/farNJrhqqn5nks63+Z0lOavUXtO+zbfuqcf1OSdKzjfPM5SDw1qpaA5wPXJFkTdv2nqpa25YdAG3bpcCPAOuBDyZZkmQJ8AHgImANcNlQP7/X+vpB4ABweatfDhxo9fe0dpKkCRlbuFTVI1X1ubb+VeABYMU8u2wAbq6q/62q/wBmgXPbMltVD1XV/wE3AxuSBHgl8PG2/1bg1UN9bW3rHwde1dpLkiZgIvdc2mWplwOfbaUrk3w+yZYky1ptBfDw0G67W+1w9e8G/quqDh5Sf0Zfbfvjrf2h49qcZCbJzL59+761HylJ+qaxh0uS7wRuBd5cVU8A1wM/AKwFHgHePe4xHE5V3VBV66pq3fLly6c1DEladMYaLkmezyBYPlpVfwFQVY9W1VNV9Q3gQwwuewHsAc4Y2n1lqx2u/hhwSpKlh9Sf0Vfb/qLWXpI0AeOcLRbgRuCBqvrDofrpQ81eA9zb1rcDl7aZXmcCq4F/Bu4EVreZYScxuOm/vaoK+DRwSdt/E3DbUF+b2volwKdae0nSBCw9cpPn7CeA1wP3JLm71X6TwWyvtUABXwR+FaCq7ktyC3A/g5lmV1TVUwBJrgR2AkuALVV1X+vv7cDNSX4H+BcGYUb7/EiSWWA/g0CSJE3I2MKlqv4RGDVDa8c8+1wLXDuivmPUflX1EE9fVhuuPwm89mjGK0nqxyf0JUndGS6SpO4MF0lSd4aLJKk7w0WS1J3hIknqznCRJHVnuEiSujNcJEndGS6SpO4MF0lSd4aLJKk7w0WS1J3hIknqznCRJHVnuEiSujNcJEndGS6SpO4MF0lSd4aLJKk7w0WS1J3hIknqznCRJHVnuEiSujNcJEndGS6SpO4MF0lSd2MLlyRnJPl0kvuT3JfkN1r9xUl2JXmwfS5r9SS5Lslsks8nOXuor02t/YNJNg3Vz0lyT9vnuiSZ7xiSpMkY55nLQeCtVbUGOB+4Iska4Crg9qpaDdzevgNcBKxuy2bgehgEBXA1cB5wLnD1UFhcD7xxaL/1rX64Y0iSJmBs4VJVj1TV59r6V4EHgBXABmBra7YVeHVb3wBsq4E7gFOSnA5cCOyqqv1VdQDYBaxv206uqjuqqoBth/Q16hiSpAmYyD2XJKuAlwOfBU6rqkfapi8Dp7X1FcDDQ7vtbrX56rtH1JnnGIeOa3OSmSQz+/btew6/TJI0ytjDJcl3ArcCb66qJ4a3tTOOGufx5ztGVd1QVeuqat3y5cvHOQxJOqGMNVySPJ9BsHy0qv6ilR9tl7Ron3tbfQ9wxtDuK1ttvvrKEfX5jiFJmoBxzhYLcCPwQFX94dCm7cDcjK9NwG1D9Y1t1tj5wOPt0tZO4IIky9qN/AuAnW3bE0nOb8faeEhfo44hSZqApWPs+yeA1wP3JLm71X4T+F3gliSXA18CXte27QAuBmaBrwFvAKiq/UneBdzZ2l1TVfvb+puAm4AXAp9sC/McQ5I0AWMLl6r6RyCH2fyqEe0LuOIwfW0BtoyozwBnjag/NuoYkqTJ8Al9SVJ3hoskqTvDRZLUneEiSerOcJEkdWe4SJK6M1wkSd0ZLpKk7gwXSVJ3hoskqTvDRZLUneEiSerOcJEkdWe4SJK6M1wkSd0ZLpKk7gwXSVJ3hoskqTvDRZLUneEiSepuQeGS5PaF1CRJAlg638Yk3wZ8O3BqkmVA2qaTgRVjHpsk6Tg1b7gAvwq8GXgJcBdPh8sTwPvHNyxJ0vFs3nCpqvcC703y61X1vgmNSZJ0nDvSmQsAVfW+JD8OrBrep6q2jWlckqTj2ILCJclHgB8A7gaeauUCDBdJ0rMsKFyAdcCaqqpxDkaStDgs9DmXe4HvPZqOk2xJsjfJvUO1dybZk+Tutlw8tO0dSWaTfCHJhUP19a02m+SqofqZST7b6n+W5KRWf0H7Ptu2rzqacUuSvnULDZdTgfuT7EyyfW45wj43AetH1N9TVWvbsgMgyRrgUuBH2j4fTLIkyRLgA8BFwBrgstYW4PdaXz8IHAAub/XLgQOt/p7WTpI0QQu9LPbOo+24qj5zFGcNG4Cbq+p/gf9IMguc27bNVtVDAEluBjYkeQB4JfCLrc3WNsbrW19z4/048P4k8ZKeJE3OQmeL/X3HY16ZZCMwA7y1qg4weCDzjqE2u3n6Ic2HD6mfB3w38F9VdXBE+xVz+1TVwSSPt/Zf6fgbJEnzWOjrX76a5Im2PJnkqSRPPIfjXc9g1tla4BHg3c+hj26SbE4yk2Rm37590xyKJC0qCwqXqvquqjq5qk4GXgj8AvDBoz1YVT1aVU9V1TeAD/H0pa89wBlDTVe22uHqjwGnJFl6SP0ZfbXtL2rtR43nhqpaV1Xrli9ffrQ/R5J0GEf9VuQa+EvgwiO1PVSS04e+vobBLDSA7cClbabXmcBq4J+BO4HVbWbYSQxu+m9v908+DVzS9t8E3DbU16a2fgnwKe+3SNJkLfQhyp8f+vo8Bs+9PHmEfT4GvILBSy93A1cDr0iylsEDmF9k8O4yquq+JLcA9wMHgSuq6qnWz5XATmAJsKWq7muHeDtwc5LfAf4FuLHVbwQ+0iYF7GcQSJKkCVrobLGfG1o/yCAYNsy3Q1VdNqJ844jaXPtrgWtH1HcAO0bUH+Lpy2rD9SeB1843NknSeC10ttgbxj0QSdLisdDZYiuTfKI9cb83ya1JVo57cJKk49NCb+h/mMGN8pe05a9aTZKkZ1louCyvqg9X1cG23AQ4d1eSNNJCw+WxJL80976vJL/EYZ4dkSRpoeHyK8DrgC8zeLL+EuCXxzQmSdJxbqFTka8BNrX3gJHkxcAfMAgdSZKeYaFnLj82FywAVbUfePl4hiRJOt4tNFyel2TZ3Jd25rLQsx5J0glmoQHxbuCfkvx5+/5aRjxNL0kSLPwJ/W1JZhj8gS6An6+q+8c3LEnS8WzBl7ZamBgokqQjOupX7kuSdCSGiySpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuDBdJUneGiySpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuxhYuSbYk2Zvk3qHai5PsSvJg+1zW6klyXZLZJJ9PcvbQPpta+weTbBqqn5PknrbPdUky3zEkSZMzzjOXm4D1h9SuAm6vqtXA7e07wEXA6rZsBq6HQVAAVwPnAecCVw+FxfXAG4f2W3+EY0iSJmRs4VJVnwH2H1LeAGxt61uBVw/Vt9XAHcApSU4HLgR2VdX+qjoA7ALWt20nV9UdVVXAtkP6GnUMSdKETPqey2lV9Uhb/zJwWltfATw81G53q81X3z2iPt8xniXJ5iQzSWb27dv3HH6OJGmUqd3Qb2ccNc1jVNUNVbWuqtYtX758nEORpBPKpMPl0XZJi/a5t9X3AGcMtVvZavPVV46oz3cMSdKETDpctgNzM742AbcN1Te2WWPnA4+3S1s7gQuSLGs38i8AdrZtTyQ5v80S23hIX6OOIUmakKXj6jjJx4BXAKcm2c1g1tfvArckuRz4EvC61nwHcDEwC3wNeANAVe1P8i7gztbumqqamyTwJgYz0l4IfLItzHMMSdKEjC1cquqyw2x61Yi2BVxxmH62AFtG1GeAs0bUHxt1DEnS5PiEviSpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuDBdJUneGiySpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuDBdJUneGiySpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuDBdJUneGiySpO8NFktSd4SJJ6m4q4ZLki0nuSXJ3kplWe3GSXUkebJ/LWj1Jrksym+TzSc4e6mdTa/9gkk1D9XNa/7Nt30z+V0rSiWuaZy4/U1Vrq2pd+34VcHtVrQZub98BLgJWt2UzcD0Mwgi4GjgPOBe4ei6QWps3Du23fvw/R5I051i6LLYB2NrWtwKvHqpvq4E7gFOSnA5cCOyqqv1VdQDYBaxv206uqjuqqoBtQ31JkiZgWuFSwN8muSvJ5lY7raoeaetfBk5r6yuAh4f23d1q89V3j6g/S5LNSWaSzOzbt+9b+T2SpCFLp3Tcn6yqPUm+B9iV5N+GN1ZVJalxD6KqbgBuAFi3bt3YjydJJ4qpnLlU1Z72uRf4BIN7Jo+2S1q0z72t+R7gjKHdV7bafPWVI+qSpAmZeLgk+Y4k3zW3DlwA3AtsB+ZmfG0Cbmvr24GNbdbY+cDj7fLZTuCCJMvajfwLgJ1t2xNJzm+zxDYO9SVJmoBpXBY7DfhEmx28FPjTqvqbJHcCtyS5HPgS8LrWfgdwMTALfA14A0BV7U/yLuDO1u6aqtrf1t8E3AS8EPhkWyRJEzLxcKmqh4CXjag/BrxqRL2AKw7T1xZgy4j6DHDWtzxYSdJzcixNRZYkLRKGiySpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuDBdJUneGiySpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuDBdJUneGiySpO8NFktSd4SJJ6s5wkSR1Z7hIkrozXCRJ3RkukqTuDBdJUneGiySpO8NFktSd4SJJ6m7RhkuS9Um+kGQ2yVXTHo8knUgWZbgkWQJ8ALgIWANclmTNdEclSSeOpdMewJicC8xW1UMASW4GNgD3T3VU0pT85zU/Ou0h6Bj0fb99z9j6XqzhsgJ4eOj7buC8Qxsl2Qxsbl//O8kXJjC2E8WpwFemPYhjQf5g07SHoGfy3+acq9Ojl5eOKi7WcFmQqroBuGHa41iMksxU1bppj0M6lP82J2NR3nMB9gBnDH1f2WqSpAlYrOFyJ7A6yZlJTgIuBbZPeUySdMJYlJfFqupgkiuBncASYEtV3TflYZ1ovNyoY5X/NicgVTXtMUiSFpnFellMkjRFhoskqTvDRV352h0dq5JsSbI3yb3THsuJwHBRN752R8e4m4D10x7EicJwUU/ffO1OVf0fMPfaHWnqquozwP5pj+NEYbiop1Gv3VkxpbFImiLDRZLUneGinnztjiTAcFFfvnZHEmC4qKOqOgjMvXbnAeAWX7ujY0WSjwH/BPxwkt1JLp/2mBYzX/8iSerOMxdJUneGiySpO8NFktSd4SJJ6s5wkSR1Z7hIU5Dke5PcnOTfk9yVZEeSH/KNvVosFuWfOZaOZUkCfALYWlWXttrLgNOmOjCpI89cpMn7GeDrVfXHc4Wq+leGXvqZZFWSf0jyubb8eKufnuQzSe5Ocm+Sn0qyJMlN7fs9Sd4y+Z8kPZNnLtLknQXcdYQ2e4Gfraonk6wGPgasA34R2FlV17a/n/PtwFpgRVWdBZDklHENXFoow0U6Nj0feH+StcBTwA+1+p3AliTPB/6yqu5O8hDw/UneB/w18LfTGLA0zMti0uTdB5xzhDZvAR4FXsbgjOUk+OYfvPppBm+bvinJxqo60Nr9HfBrwJ+MZ9jSwhku0uR9CnhBks1zhSQ/xjP/XMGLgEeq6hvA64Elrd1LgUer6kMMQuTsJKcCz6uqW4HfAs6ezM+QDs/LYtKEVVUleQ3wR0neDjwJfBF481CzDwK3JtkI/A3wP63+CuBtSb4O/DewkcFf+/xwkrn/LL5j3L9BOhLfiixJ6s7LYpKk7gwXSVJ3hoskqTvDRZLUneEiSerOcJEkdWe4SJK6+3+NdjIPZ/6YAwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Class\", data=creditcard)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import imblearn\n",
    "from imblearn.under_sampling import RandomUnderSampler \n",
    "\n",
    "undersample = RandomUnderSampler(sampling_strategy=0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "cols = creditcard.columns.tolist()\n",
    "cols = [c for c in cols if c not in [\"Class\"]]\n",
    "target = \"Class\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = creditcard[cols]\n",
    "Y = creditcard[target]\n",
    "\n",
    "\n",
    "X_under, Y_under = undersample.fit_resample(X, Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pandas import DataFrame\n",
    "test = pd.DataFrame(Y_under, columns = ['Class'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'After')"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 936x324 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axs = plt.subplots(ncols=2, figsize=(13,4.5))\n",
    "sns.countplot(x=\"Class\", data=creditcard, ax=axs[0])\n",
    "sns.countplot(x=\"Class\", data=test, ax=axs[1])\n",
    "\n",
    "fig.suptitle(\"Class repartition before and after undersampling\")\n",
    "a1=fig.axes[0]\n",
    "a1.set_title(\"Before\")\n",
    "a2=fig.axes[1]\n",
    "a2.set_title(\"After\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X_under, Y_under, test_size=0.2, random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from xgboost import XGBClassifier\n",
    "from sklearn.neural_network import MLPClassifier\n",
    "\n",
    "from sklearn import metrics\n",
    "from sklearn.metrics import confusion_matrix\n",
    "from sklearn.metrics import roc_curve\n",
    "from sklearn.metrics import roc_auc_score\n",
    "from sklearn.metrics import auc\n",
    "from sklearn.metrics import precision_recall_curve"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "model1 = LogisticRegression(random_state=2)\n",
    "logit = model1.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred_logit = model1.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy Logit: 0.9493243243243243\n",
      "Precision Logit: 0.9603960396039604\n",
      "Recall Logit: 0.8981481481481481\n",
      "F1 Score Logit: 0.9282296650717703\n"
     ]
    }
   ],
   "source": [
    "print(\"Accuracy Logit:\",metrics.accuracy_score(y_test, y_pred_logit))\n",
    "print(\"Precision Logit:\",metrics.precision_score(y_test, y_pred_logit))\n",
    "print(\"Recall Logit:\",metrics.recall_score(y_test, y_pred_logit))\n",
    "print(\"F1 Score Logit:\",metrics.f1_score(y_test, y_pred_logit))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "matrix_logit = confusion_matrix(y_test, y_pred_logit)\n",
    "cm_logit = pd.DataFrame(matrix_logit, index=['not_fraud', 'fraud'], columns=['not_fraud', 'fraud'])\n",
    "\n",
    "sns.heatmap(cm_logit, annot=True, cbar=None, cmap=\"Blues\", fmt = 'g')\n",
    "plt.title(\"Confusion Matrix Logit\"), plt.tight_layout()\n",
    "plt.ylabel(\"True Class\"), plt.xlabel(\"Predicted Class\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AUC Logistic Regression : 0.9700059101654847\n"
     ]
    }
   ],
   "source": [
    "y_pred_logit_proba = model1.predict_proba(X_test)[::,1]\n",
    "fpr_logit, tpr_logit, _ = metrics.roc_curve(y_test,  y_pred_logit_proba)\n",
    "auc_logit = metrics.roc_auc_score(y_test, y_pred_logit_proba)\n",
    "print(\"AUC Logistic Regression :\", auc_logit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(fpr_logit,tpr_logit,label=\"Logistic Regression, auc={:.3f})\".format(auc_logit))\n",
    "plt.plot([0, 1], [0, 1], 'k--')\n",
    "plt.xlabel('False positive rate')\n",
    "plt.ylabel('True positive rate')\n",
    "plt.title('Logistic Regression ROC curve')\n",
    "plt.legend(loc=4)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "logit_precision, logit_recall, _ = precision_recall_curve(y_test, y_pred_logit_proba)\n",
    "no_skill = len(y_test[y_test==1]) / len(y_test)\n",
    "plt.plot([0, 1], [no_skill, no_skill], linestyle='--', color='black', label='No Skill')\n",
    "plt.plot(logit_recall, logit_precision, color='orange', label='Logistic')\n",
    "plt.xlabel('Recall')\n",
    "plt.ylabel('Precision')\n",
    "plt.title('Precision-Recall curve')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}