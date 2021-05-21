%Lecture des fichiers
data= readtable('g13_data.csv');
%Nombre de joueurs
numberOfPlayer=height(data);

lightScore1 = data(:,3);
lightScore2 = data(:,4);
lightScore3 = data(:,5);
lightScore1=cell2mat(table2cell(lightScore1));
lightScore2=cell2mat(table2cell(lightScore2));
lightScore3=cell2mat(table2cell(lightScore3));

soundScore1=cell2mat(table2cell(data(:,6)));
soundScore2=cell2mat(table2cell(data(:,7)));
soundScore3=cell2mat(table2cell(data(:,8)));

memoryWrongAns=data(:,9);

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

%Best score
bestLightScore=zeros(numberOfPlayer,1);
for i=1:numberOfPlayer
    bestLightScore(i,1)=max(cell2mat(table2cell(data(i,3:5))))*1000;
end