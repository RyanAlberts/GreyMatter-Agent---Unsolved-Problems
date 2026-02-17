"use client"

import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Bar, BarChart, ResponsiveContainer, XAxis, YAxis, Tooltip } from "recharts"
import { motion } from "framer-motion"

type Verification = {
    is_novel: boolean
    tam_estimate: string
    leading_labs: string[]
    complexity_score: number
}

type Problem = {
    topic: string
    problem_statement: string
    source: string
    importance_justification: string
    importance_score: number
    verification: Verification
    date?: string
}

export default function Dashboard({ data }: { data: Problem[] }) {
    // Parse TAM for charting
    const chartData = data.slice(0, 10).map(item => ({
        name: item.topic.split(" ")[0],
        tam: parseInt(item.verification.tam_estimate.replace(/[^0-9]/g, "")) || 0,
        score: item.importance_score
    }))

    // Split into lists
    // 1. All Time Sorted (already sorted by backend, but safety check)
    const allTime = [...data].sort((a, b) => b.importance_score - a.importance_score).slice(0, 20);

    // 2. Today's Findings (assuming 'today' is the latest date in the dataset)
    // In a real app we'd compare against actual today, but for demo we take the latest date found
    const dates = data.map(d => d.date).filter(Boolean).sort();
    const latestDate = dates[dates.length - 1];
    const todaysFindings = data.filter(d => d.date === latestDate);

    return (
        <div className="space-y-12">
            {/* Hero Section: Top Problems */}
            <section className="space-y-6">
                <h2 className="text-3xl font-bold tracking-tight">Top Unsolved Problems (All Time)</h2>
                <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                    {allTime.map((problem, index) => (
                        <ProblemCard key={index} problem={problem} index={index} />
                    ))}
                </div>
            </section>

            {/* Analytics */}
            <section className="space-y-6">
                <h2 className="text-2xl font-bold tracking-tight">Market & Complexity Analysis</h2>
                <div className="grid gap-4 md:grid-cols-2">
                    <Card>
                        <CardHeader>
                            <CardTitle>Market Opportunity (TAM)</CardTitle>
                            <CardDescription>Billions USD</CardDescription>
                        </CardHeader>
                        <CardContent>
                            <ResponsiveContainer width="100%" height={300}>
                                <BarChart data={chartData}>
                                    <XAxis dataKey="name" stroke="#888888" fontSize={12} tickLine={false} axisLine={false} />
                                    <YAxis stroke="#888888" fontSize={12} tickLine={false} axisLine={false} />
                                    <Tooltip contentStyle={{ background: "#333", border: "none", color: "#fff" }} cursor={{ fill: 'transparent' }} />
                                    <Bar dataKey="tam" fill="#adfa1d" radius={[4, 4, 0, 0]} />
                                </BarChart>
                            </ResponsiveContainer>
                        </CardContent>
                    </Card>
                </div>
            </section>

            {/* Latest Findings */}
            <section className="space-y-6">
                <div className="flex items-center justify-between">
                    <h2 className="text-2xl font-bold tracking-tight">Latest Findings ({latestDate})</h2>
                </div>
                <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                    {todaysFindings.map((problem, index) => (
                        <ProblemCard key={index} problem={problem} />
                    ))}
                </div>
            </section>
        </div>
    )
}

function ProblemCard({ problem, index }: { problem: Problem, index?: number }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
        >
            <Card className="h-full flex flex-col border-2 border-transparent hover:border-primary/20 transition-all">
                <CardHeader>
                    <div className="flex justify-between items-start gap-2">
                        <Badge variant={problem.importance_score > 90 ? "destructive" : "secondary"}>
                            Score: {problem.importance_score}
                        </Badge>
                        {index !== undefined && index < 3 && (
                            <span className="text-4xl font-black text-muted/20">#{index + 1}</span>
                        )}
                    </div>
                    <CardTitle className="leading-snug text-lg mt-2">{problem.problem_statement}</CardTitle>
                    <CardDescription className="font-mono text-xs mt-1">Topic: {problem.topic}</CardDescription>
                </CardHeader>
                <CardContent className="flex-grow space-y-4">
                    <div className="bg-muted/50 p-3 rounded-md text-sm italic">
                        "{problem.importance_justification}"
                    </div>

                    <div className="space-y-2">
                        <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">Identified By</p>
                        <div className="flex items-center gap-2">
                            <span className="text-sm font-medium">{problem.source}</span>
                        </div>
                    </div>

                    <div className="pt-2 flex flex-wrap gap-2">
                        {problem.verification.leading_labs.map((lab) => (
                            <Badge key={lab} variant="outline" className="text-[10px]">{lab}</Badge>
                        ))}
                        <Badge variant="outline" className="text-[10px] bg-green-500/10 text-green-700 border-green-200">
                            TAM: {problem.verification.tam_estimate}
                        </Badge>
                    </div>
                </CardContent>
            </Card>
        </motion.div>
    )
}
