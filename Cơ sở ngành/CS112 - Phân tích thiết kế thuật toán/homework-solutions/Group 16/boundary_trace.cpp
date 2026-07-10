#include <bits/stdc++.h>
using namespace std;

struct Vec {
    float x, y;
    Vec operator+(const Vec &o) const { return {x+o.x, y+o.y}; }
    Vec operator-(const Vec &o) const { return {x-o.x, y-o.y}; }
    Vec operator*(float k) const { return {x*k, y*k}; }
};

inline float cross(const Vec &a, const Vec &b) { return a.x*b.y - a.y*b.x; }
inline float dot(const Vec &a, const Vec &b) { return a.x*b.x + a.y*b.y; }
inline float len(const Vec &a) { return sqrt(dot(a,a)); }
inline Vec norm(const Vec &a) { float l=len(a); return l>1e-6? Vec{a.x/l,a.y/l} : Vec{0,0}; }

vector<Vec> convexHull(vector<Vec> pts) {
    sort(pts.begin(), pts.end(), [](auto &a, auto &b){
        return a.x != b.x ? a.x < b.x : a.y < b.y;
    });
    pts.erase(unique(pts.begin(), pts.end(), [](auto&a,auto&b){
        return fabs(a.x-b.x)<1e-6 && fabs(a.y-b.y)<1e-6;
    }), pts.end());
    if(pts.size() < 3) return pts;

    vector<Vec> hull;
    // lower hull
    for(auto &p : pts) {
        while(hull.size() >= 2 && cross(hull[hull.size()-1] - hull[hull.size()-2], p - hull[hull.size()-1]) <= 0)
            hull.pop_back();
        hull.push_back(p);
    }
    // upper hull
    int lower_size = hull.size();
    for(int i = pts.size()-2; i >= 0; i--) {
        while(hull.size() > lower_size && cross(hull[hull.size()-1] - hull[hull.size()-2], pts[i] - hull[hull.size()-1]) <= 0)
            hull.pop_back();
        hull.push_back(pts[i]);
    }
    hull.pop_back();
    return hull;
}

vector<Vec> expandHull(const vector<Vec> &hull, float dist) {
    if(hull.size() < 3) return hull;
    
    Vec center = {0, 0};
    for(auto &p : hull) {
        center.x += p.x;
        center.y += p.y;
    }
    center.x /= hull.size();
    center.y /= hull.size();
    
    vector<Vec> expanded;
    for(auto &p : hull) {
        Vec dir = norm(p - center);
        expanded.push_back(p + dir * dist);
    }
    return expanded;
}

vector<Vec> bossPositions;
vector<Vec> visitedPoints; 
vector<Vec> patrolPath;         
Vec specialZoneCenter = {0, 0};
bool foundSpecialZone = false;
float angle = 0;
int currentPatrolIndex = 0;    
float expansionDistance = 80.0f; 

Vec getNextPoint(float x, float y, int lastBossID) {
    Vec currentPos = {x, y};
    visitedPoints.push_back(currentPos);
    
    if(lastBossID != 0)
        bossPositions.push_back(currentPos);
    

    if(lastBossID == 36) {
        if(!foundSpecialZone) {
            foundSpecialZone = true;
            specialZoneCenter = currentPos;
        } else {
            Vec sum = {0, 0};
            int count = 0;
            for(auto &pos : bossPositions) {
                sum = sum + pos;
                count++;
            }
            if(count > 0) {
                specialZoneCenter.x = sum.x / count;
                specialZoneCenter.y = sum.y / count;
            }
        }
    }
    
    if(foundSpecialZone) {
        angle += 0.5f;
        float radius = 80 + angle * 60;
        return Vec{
            specialZoneCenter.x + radius * cos(angle),
            specialZoneCenter.y + radius * sin(angle)
        };
    } else {
        if(visitedPoints.size() >= 3 && visitedPoints.size() % 5 == 0) {
            auto hull = convexHull(visitedPoints);
            if(hull.size() >= 3) {
                patrolPath = expandHull(hull, expansionDistance);
                currentPatrolIndex = 0;
            }
        }
        
        if(!patrolPath.empty()) {
            Vec target = patrolPath[currentPatrolIndex];
            currentPatrolIndex = (currentPatrolIndex + 1) % patrolPath.size();
            return target;
        } else {
            angle += 0.5f;
            float radius = 80 + angle * 60;
            return Vec{
                currentPos.x + radius * cos(angle),
                currentPos.y + radius * sin(angle)
            };
        }
    }
}

int main() {

}