function [asc_avg_wind_speed des_avg_wind_speed asc_avg_wind_vel_u...
des_avg_wind_vel_u asc_avg_wind_vel_v des_avg_wind_vel_v...
asc_avg_wind_speed_sq des_avg_wind_speed_sq asc_wvc_count des_wvc_count...
asc_time_frac des_time_frac asc_rain_prob des_rain_prob asc_rain_flag...
des_rain_flag]=read_QuikSCAT_L3(fnam)

% This program reads Level 3 QuikSCAT data.  The input, fnam, is the file
% name of the desired data file to be read, including path if the read 
% software and data are in different folders.  The output is 16 variables,
% which are the parameters found in the data file.  The ascending variables
% start with asc and descending with des.
%
% The file being read must be unzipped, this program will not do it for you.
%
% scaling is applied at the end of the program.  If you do not want scaling
% applied comment out lines 54-82
%
% To execute this program type the following text at the MATLAB command prompt
%  [asc_avg_wind_speed des_avg_wind_speed asc_avg_wind_vel_u...
%  des_avg_wind_vel_u asc_avg_wind_vel_v des_avg_wind_vel_v...
%  asc_avg_wind_speed_sq des_avg_wind_speed_sq asc_wvc_count des_wvc_count...
%  asc_time_frac des_time_frac asc_rain_prob des_rain_prob asc_rain_flag...
%  des_rain_flag]=read_QuikSCAT_L3(fnam);
%
% Replace "fnam" with the actual file name and directory location.
% Use single quotes (' ') around the file name.
%
% The above command will return all 16 variables in the [] into the workspace.
%
% Documentation can be found at:
%  ftp://podaac.jpl.nasa.gov/pub/ocean_wind/quikscat/L3/doc/qscat_L3.html
%
% Program Language: MATLAB
%
% Program Author: Jessica Hausman
% Program Co-Author: David F. Moroni
%
%Copyright (c) 2010 California Institute of Technology
%
% Revisions:	Date		Author		Description
%
%	    1/8/2010	    J. Hausman		    Created.
%	    1/8/2010	     D. Moroni   Additonal Comments.


%read attributes 
qsinfo=hdfinfo(fnam);   %find attributes in qsinfo.Attributes

%read data
asc_avg_wind_speed=hdfread(fnam,'asc_avg_wind_speed');
des_avg_wind_speed=hdfread(fnam,'des_avg_wind_speed');
asc_avg_wind_vel_u=hdfread(fnam,'asc_avg_wind_vel_u');
des_avg_wind_vel_u=hdfread(fnam,'des_avg_wind_vel_u');
asc_avg_wind_vel_v=hdfread(fnam,'asc_avg_wind_vel_v');
des_avg_wind_vel_v=hdfread(fnam,'des_avg_wind_vel_v');
asc_avg_wind_speed_sq=hdfread(fnam,'asc_avg_wind_speed_sq');
des_avg_wind_speed_sq=hdfread(fnam,'des_avg_wind_speed_sq');
asc_wvc_count=hdfread(fnam,'asc_wvc_count');
des_wvc_count=hdfread(fnam,'des_wvc_count');
asc_time_frac=hdfread(fnam,'asc_time_frac');
des_time_frac=hdfread(fnam,'des_time_frac');
asc_rain_prob=hdfread(fnam,'asc_rain_prob');
des_rain_prob=hdfread(fnam,'des_rain_prob');
asc_rain_flag=hdfread(fnam,'asc_rain_flag');    %see documentation for flag values
des_rain_flag=hdfread(fnam,'des_rain_flag');    %ftp://podaac.jpl.nasa.gov/pub/ocean_wind/quikscat/L3/doc/qscat_L3.html

%make all parameter type double and apply scaling if applicable
asc_avg_wind_speed=double(asc_avg_wind_speed);
des_avg_wind_speed=double(des_avg_wind_speed);
asc_avg_wind_vel_u=double(asc_avg_wind_vel_u);
des_avg_wind_vel_u=double(des_avg_wind_vel_u);
asc_avg_wind_vel_v=double(asc_avg_wind_vel_v);
des_avg_wind_vel_v=double(des_avg_wind_vel_v);
asc_avg_wind_speed_sq=double(asc_avg_wind_speed_sq);
des_avg_wind_speed_sq=double(des_avg_wind_speed_sq);
asc_wvc_count=double(asc_wvc_count);
des_wvc_count=double(des_wvc_count);
asc_time_frac=double(asc_time_frac);
des_time_frac=double(des_time_frac);
asc_rain_prob=double(asc_rain_prob);
des_rain_prob=double(des_rain_prob);

asc_avg_wind_speed=asc_avg_wind_speed.*0.01;    %units=m/s
des_avg_wind_speed=des_avg_wind_speed.*0.01;    %m/s
asc_avg_wind_vel_u=asc_avg_wind_vel_u.*0.01;    %m/s
des_avg_wind_vel_u=des_avg_wind_vel_u.*0.01;    %m/s
asc_avg_wind_vel_v=asc_avg_wind_vel_v.*0.01;    %m/s
des_avg_wind_vel_v=des_avg_wind_vel_v.*0.01;    %m/s
asc_avg_wind_speed_sq=asc_avg_wind_speed_sq.*0.01;  %(m/s)^2
des_avg_wind_speed_sq=des_avg_wind_speed_sq.*0.01;  %(m/s)^2
asc_time_frac=asc_time_frac.*0.00002;   %fraction of day (UTC)
des_time_frac=des_time_frac.*0.00002;   %fraction of day (UTC)
asc_rain_prob=asc_rain_prob.*0.001;
des_rain_prob=des_rain_prob.*0.001;

