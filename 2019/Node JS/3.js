#!/usr/bin/env node
const fs = require('fs');
const assert = require('assert');

const wires = fs
    .readFileSync(0, 'utf-8')
    .trim()
    .split('\n')
    .map(x => parseWire(x));

const intersections = [...findIntersections(wires[0].verticalLines, wires[1].horizontalLines), ...findIntersections(wires[1].verticalLines, wires[0].horizontalLines)];

// part one
console.log(Math.min(...intersections.map(([x, y]) => Math.abs(x) + Math.abs(y))));

// part two
const summedLengthsToIntersections = wires.map(wire => lengthsToIntersections(wire, intersections)).reduce((summedLenghts, lengths) => {
    const newLengths = {};
    Object.keys(lengths).forEach(key => newLengths[key] = summedLenghts[key] + lengths[key]);
    return newLengths;
})
console.log(Math.min(...Object.values(summedLengthsToIntersections)));

//

function parseWire(path) {
    const verticalLines = [];
    const horizontalLines = [];
    const segmentChanges = [];

    let lastPoint = [0, 0];

    const pathSegments = path.split(',');
    for (const pathSegment of pathSegments) {
        const direction = pathSegment[0];
        const length = parseInt(pathSegment.substring(1));

        assert(length > 0);

        const nextPoint = [...lastPoint];
        switch (direction) {
            case 'U':
                nextPoint[1] = lastPoint[1] + length;
                verticalLines.push([lastPoint, nextPoint]);
                segmentChanges.push([0, length]);
                break;
            case 'R':
                nextPoint[0] = lastPoint[0] + length;
                horizontalLines.push([lastPoint, nextPoint]);
                segmentChanges.push([length, 0]);
                break;
            case 'D':
                nextPoint[1] = lastPoint[1] - length;
                verticalLines.push([nextPoint, lastPoint]);
                segmentChanges.push([0, -length]);
                break;
            case 'L':
                nextPoint[0] = lastPoint[0] - length;
                horizontalLines.push([nextPoint, lastPoint]);
                segmentChanges.push([-length, 0]);
                break;
        }
        lastPoint = nextPoint;
    }

    assert(verticalLines.length + horizontalLines.length === pathSegments.length);
    assert(segmentChanges.length === pathSegments.length);

    return { verticalLines, horizontalLines, segmentChanges };
}

function findIntersections(verticalLines, horizontalLines) {
    const intersections = [];
    for (const [[vx1, vy1], [vx2, vy2]] of verticalLines) {
        assert(vx1 == vx2);
        for (const [[hx1, hy1], [hx2, hy2]] of horizontalLines) {
            assert(hy1 == hy2);
            if (hx1 < vx1 && vx1 < hx2 && vy1 < hy1 && hy1 < vy2) {
                intersections.push([vx1, hy1]);
            }
        }
    }
    return intersections;
}

function lengthsToIntersections(wire, intersections) {
    const point = [0, 0];
    const lengths = {};
    let totalLength = 0;

    for (const change of wire.segmentChanges) {
        assert(change[0] === 0 || change[1] === 0);
        const [y0, y1] = sortNumerically([point[1], point[1] + change[1]]);
        const [x0, x1] = sortNumerically([point[0], point[0] + change[0]]);
        intersections.filter(is => (is[0] === point[0] && y0 < is[1] && is[1] < y1) || (is[1] === point[1] && x0 < is[0] && is[0] < x1)).map(intersection => {
            if (!lengths[intersection]) {
                lengths[intersection] = totalLength + Math.abs(intersection[0] - point[0]) + Math.abs(intersection[1] - point[1]);
            }
        });
        point[0] += change[0];
        point[1] += change[1];
        totalLength += Math.abs(change[0]) + Math.abs(change[1]);
    }

    assert(Object.keys(lengths).length === intersections.length, 'not all intersections have been reached');

    return lengths
}

function sortNumerically(arr) {
    return arr.sort((a, b) => a - b);
}
