%Lecture des fichiers
rawData= readtable('g13_data.csv');
data=table2cell(rawData);
%Nombre de joueurs
numberOfPlayer=height(data);

lightScore1=cell2mat(data(:,3));    %Score 1 lumière
lightScore2=cell2mat(data(:,4));    %Score 2 lumière
lightScore3=cell2mat(data(:,5));    %Score 3 lumière

soundScore1=cell2mat(data(:,6));    %Score 1 son
soundScore2=cell2mat(data(:,7));    %Score 2 son
soundScore3=cell2mat(data(:,8));    %Score 3 son

memoryWrongAns=cell2mat(data(:,9));   %Nombre d'erreurs
memoryRightAns=32-memoryWrongAns; %Nombre justes
rightPourcentage=memoryRightAns/32*100; %Pourcentage juste

averageLightScore=zeros(numberOfPlayer,1);
%Average reaction time LIGHTS
for i=1:numberOfPlayer
    averageLightScore(i,1)=lightScore1(i,1)+lightScore2(i,1)+lightScore3(i,1);
end
averageLightScore=averageLightScore/3*1000; %En ms

averageSoundScore=zeros(numberOfPlayer,1);
%Average reaction time SOUND
for i=1:numberOfPlayer
    averageSoundScore(i,1)=soundScore1(i,1)+soundScore2(i,1)+soundScore3(i,1);
end
averageSoundScore=averageSoundScore/3*1000; %En ms

%Best light score in ms
bestLightScore=zeros(numberOfPlayer,1);
for i=1:numberOfPlayer
    bestLightScore(i,1)=min(cell2mat(data(i,3:5)))*1000;
end

%Best sound score in ms
bestSoundScore=zeros(numberOfPlayer,1);
for i=1:numberOfPlayer
    bestSoundScore(i,1)=min(cell2mat(data(i,6:8)))*1000;
end

histogram(bestLightScore,5)
title("Comparaison: best light score, best sound score")
xlabel('Reaction Time in ms')
ylabel('Number of players')
hold on
histogram(bestSoundScore,5)
legend('Light score','Sound score')

% histogram(averageLightScore,5)
% title("Comparaison: mean light score, mean sound score")
% xlabel('Reaction Time in ms')
% ylabel('Number of players')
% hold on
% histogram(averageSoundScore,5)
% legend('Light score','Sound score')

clear lightScore*
clear soundScore*
clear data*
clear numberOfPlayer*
clear i*