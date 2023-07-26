import pandas as pd



def calculate_depression_type(row):
    scores = {
        'Major Depression': (row['Genetic'] + row['Psychological stressors'] +
                             row['Lost of interest'] + row['Feeling of worthlessness']) * (70/100) + \
                            (row['Personality'] + row['Seasonal changes'] + row['Harmonal changes'] +
                             row['Hallucinations'] + row['Sleeping sickness'] +
                             row['Change in energy levels'] + row['Physical Illness'] + row['Gender']) * (30/100),

        'Persistent Depressive Disorder (PDD)': (row['Genetic'] +
                                                 row['Psychological stressors'] +
                                                 row['Personality'] + row['Sleeping sickness']) * (70/100) + \
                                                (row['Lost of interest'] + row['Seasonal changes'] +
                                                 row['Harmonal changes'] + row['Hallucinations'] +
                                                 row['Change in energy levels'] + row['Physical Illness'] +
                                                 row['Gender'] + row['Feeling of worthlessness']) * (30/100),

        'Bipolar Disorder (with depressive episodes)': (row['Genetic'] + row['Physical Illness'] +
                                                        row['Psychological stressors'] +
                                                        row['Change in energy levels'] +
                                                        row['Hallucinations']) * (70/100) + \
                                                       (row['Gender'] + row['Personality'] +
                                                        row['Lost of interest'] + row['Sleeping sickness'] +
                                                        row['Seasonal changes'] + row['Harmonal changes'] +
                                                        row['Feeling of worthlessness']) * (30/100),

        'Seasonal Affective Disorder (SAD)': (row['Genetic'] + row['Seasonal changes'] +
                                              row['Physical Illness'] + row['Sleeping sickness']) * (70/100) + \
                                             (row['Gender'] + row['Personality'] + row['Lost of interest'] +
                                              row['Harmonal changes'] + row['Feeling of worthlessness'] +
                                              row['Psychological stressors'] +
                                              row['Change in energy levels'] +
                                              row['Hallucinations']) * (30/100),

        'Psychotic Depression': (row['Genetic'] + row['Harmonal changes'] +
                                 row['Psychological stressors'] +
                                 row['Lost of interest'] + row['Feeling of worthlessness']) * (70/100) + \
                                (row['Gender'] + row['Personality'] +
                                 row['Physical Illness'] +
                                 row['Change in energy levels'] +
                                 row['Hallucinations'] + row['Seasonal changes'] +
                                 row['Sleeping sickness']) * (30/100),

        'Premenstrual Dysphoric Disorder (PMDD)': (row['Genetic'] + row['Harmonal changes'] +
                                                   row['Psychological stressors'] +
                                                   row['Gender']) * (70/100) + \
                                                  (row['Lost of interest'] + row['Seasonal changes'] +
                                                   row['Change in energy levels'] +
                                                   row['Physical Illness'] + row['Hallucinations'] +
                                                   row['Sleeping sickness'] + row['Feeling of worthlessness']) * (30/100),

        'Atypical Depression': (row['Genetic'] + row['Psychological stressors'] +
                                row['Lost of interest'] + row['Feeling of worthlessness'] +
                                row['Sleeping sickness']) * (70/100) + \
                               (row['Personality'] + row['Seasonal changes'] + row['Harmonal changes'] +
                                row['Hallucinations'] + row['Change in energy levels'] +
                                row['Physical Illness'] + row['Gender']) * (30/100),

        'Situational Depression (Reactive Depression/Adjustment Disorder)': \
            (row['Psychological stressors'] + row['Lost of interest'] +
             row['Feeling of worthlessness']) * (70/100) + \
            (row['Seasonal changes'] + row['Harmonal changes'] + row['Change in energy levels'] +
             row['Physical Illness'] + row['Hallucinations'] + row['Sleeping sickness'] +
             row['Genetic'] + row['Personality'] + row['Gender']) * (30/100)
    }

    row['score'] = max(scores.values())
    row['score2'] = max(list(scores.values())[-2:])
    row['type'] = max(scores, key=scores.get)
   

    return row

# Accept user input for depression-related factors

# Display the results
# print("Depression Type: ", df['type'].values[0])
# print("Score: ", df['score'].values[0])
