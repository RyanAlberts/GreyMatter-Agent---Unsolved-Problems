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
    source: string
    description: string
    verification: Verification
}

export default function Dashboard({ data }: { data: Problem[] }) {
    // Parse TAM for charting (remove $ and B, crude parsing)
    const chartData = data.map(item => ({
        name: item.topic.split(" ")[0], // Short name
        tam: parseInt(item.verification.tam_estimate.replace(/[^0-9]/g, "")) || 0,
        complexity: item.verification.complexity_score
    }))

    return (
        <div className="space-y-8">
            {/* Overview Charts */}
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
                <Card className="col-span-4">
                    <CardHeader>
                        <CardTitle>Market Opportunity (TAM)</CardTitle>
                        <CardDescription>
                            Estimated Total Addressable Market in Billions (USD)
                        </CardDescription>
                    </CardHeader>
                    <CardContent className="pl-2">
                        <ResponsiveContainer width="100%" height={300}>
                            <BarChart data={chartData}>
                                <XAxis
                                    dataKey="name"
                                    stroke="#888888"
                                    fontSize={12}
                                    tickLine={false}
                                    axisLine={false}
                                />
                                <YAxis
                                    stroke="#888888"
                                    fontSize={12}
                                    tickLine={false}
                                    axisLine={false}
                                    tickFormatter={(value) => `$${value}B`}
                                />
                                <Tooltip
                                    contentStyle={{ background: "#333", border: "none", borderRadius: "8px", color: "#fff" }}
                                    cursor={{ fill: 'transparent' }}
                                />
                                <Bar dataKey="tam" fill="#adfa1d" radius={[4, 4, 0, 0]} />
                            </BarChart>
                        </ResponsiveContainer>
                    </CardContent>
                </Card>
                <Card className="col-span-3">
                    <CardHeader>
                        <CardTitle>Complexity Score</CardTitle>
                        <CardDescription>
                            Technical difficulty (1-10)
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <div className="space-y-4">
                            {data.map((item, i) => (
                                <div key={i} className="flex items-center">
                                    <div className="w-full flex-1 space-y-1">
                                        <p className="text-sm font-medium leading-none">{item.topic}</p>
                                        <p className="text-xs text-muted-foreground">{item.source}</p>
                                    </div>
                                    <div className="ml-auto font-bold">
                                        {item.verification.complexity_score}/10
                                    </div>
                                </div>
                            ))}
                        </div>
                    </CardContent>
                </Card>
            </div>

            {/* Detailed Cards */}
            <h2 className="text-3xl font-bold tracking-tight">Identified Unsolved Problems</h2>
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                {data.map((problem, index) => (
                    <motion.div
                        key={index}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.1 }}
                    >
                        <Card className="h-full flex flex-col">
                            <CardHeader>
                                <div className="flex justify-between items-start">
                                    <CardTitle className="leading-snug">{problem.topic}</CardTitle>
                                    <Badge variant="secondary">{problem.verification.tam_estimate}</Badge>
                                </div>
                                <CardDescription className="line-clamp-2">{problem.source}</CardDescription>
                            </CardHeader>
                            <CardContent className="flex-grow">
                                <p className="text-sm text-foreground/80">{problem.description}</p>
                                <div className="mt-4 flex flex-wrap gap-2">
                                    {problem.verification.leading_labs.map((lab) => (
                                        <Badge key={lab} variant="outline" className="text-[10px]">{lab}</Badge>
                                    ))}
                                </div>
                            </CardContent>
                            <CardFooter className="pt-0 text-xs text-muted-foreground">
                                Verified Novelty: {problem.verification.is_novel ? "Yes" : "No"}
                            </CardFooter>
                        </Card>
                    </motion.div>
                ))}
            </div>
        </div>
    )
}
