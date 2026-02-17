import fs from 'fs'
import path from 'path'
import Dashboard from '@/components/Dashboard'

async function getData() {
  const filePath = path.join(process.cwd(), 'public', 'report.json')
  try {
    const fileContents = fs.readFileSync(filePath, 'utf8')
    return JSON.parse(fileContents)
  } catch (error) {
    console.error("Error reading report.json", error)
    return []
  }
}

export default async function Page() {
  const data = await getData()

  return (
    <div className="flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <h2 className="text-lg font-semibold">GreyMatter AI</h2>
          <div className="ml-auto flex items-center space-x-4">
            <span className="text-sm text-muted-foreground">Autonomous Research Agent</span>
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Dashboard</h2>
        </div>
        <Dashboard data={data} />
      </div>
    </div>
  )
}
